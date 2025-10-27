# -*- coding: utf-8 -*-
"""
Digi-Key Product Info v4 lookup (OAuth2 client-credentials).
- Reusable API function: fetch_digikey_parts(...)
- Optional CLI: read queries from a file and write CSV.

Env:
  DK_CLIENT_ID=...
  DK_CLIENT_SECRET=...
  # Optional:
  DK_USE_SANDBOX=true|false

Usage (CLI):
  python pcb_prototyping/scripts/digikey_lookup.py --in bom_queries.txt --out digikey_quote.csv
  # or:
  python pcb_prototyping/scripts/digikey_lookup.py --queries "ESP32-S3-WROOM-1-N16R8" "MAX98357AETE+T"

Input format:
- Plain text file with one query per line (MPN, DKPN or keyword).
- Or pass queries as CLI args.

Author: PF Design Labs / FabOps
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import quote, urlparse

try:
    from dotenv import load_dotenv

    load_dotenv()  # loads .env if present
except Exception:
    pass

import requests


# ----------------------- Config -----------------------

BASE_AUTH = "https://api-accounts.digikey.com"
BASE_API_PROD = "https://api.digikey.com/services/partsearch/v4"
BASE_API_SANDBOX = "https://sandbox-api.digikey.com/services/partsearch/v4"

DEFAULT_TIMEOUT = 30
DEFAULT_LIMIT = 8
MAX_RETRIES = 3

CAD_TYPE_ALIASES: Dict[str, Tuple[str, ...]] = {
    "symbol": ("symbol", "schematic", "schematic symbol"),
    "footprint": ("footprint", "land pattern", "layout"),
    "step": ("step", "3d", "3d model", "model"),
}
CAD_PRIMARY_TYPES = {"symbol", "footprint", "step"}
CAD_CONTAINER_KEYS = (
    "ProductUrls",
    "ProductDocuments",
    "Datasheets",
    "Documents",
    "Media",
    "Downloads",
    "SupplementaryUrls",
    "SupportingDocuments",
    "ProductFiles",
)


@dataclass
class CADResource:
    provider: str
    asset_type: str
    url: str
    description: str = ""
    local_path: Optional[str] = None


def _normalize_cad_type(label: Optional[str]) -> str:
    if not label:
        return "other"
    lowered = label.lower()
    for canonical, aliases in CAD_TYPE_ALIASES.items():
        if canonical in lowered:
            return "step" if canonical == "step" else canonical
        if any(alias in lowered for alias in aliases):
            return "step" if canonical == "step" else canonical
    if "step" in lowered or "3d" in lowered:
        return "step"
    if "symbol" in lowered:
        return "symbol"
    if "footprint" in lowered or "land" in lowered:
        return "footprint"
    return "other"


def _sanitize_filename(name: str, default: str = "cad_asset") -> str:
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", (name or "").strip())
    sanitized = sanitized.strip("._")
    return sanitized or default


def _append_resource(
    resources: List[CADResource],
    seen: set,
    *,
    url: Optional[str],
    provider: str,
    description: str,
    asset_type: str,
    local_path: Optional[str] = None,
) -> None:
    if not url or url in seen:
        return
    seen.add(url)
    resources.append(
        CADResource(
            provider=provider,
            asset_type=asset_type,
            url=url,
            description=description,
            local_path=local_path,
        )
    )


def _collect_resources_from_container(
    container: Dict[str, Any],
    *,
    provider: str,
    seen: set,
) -> List[CADResource]:
    collected: List[CADResource] = []
    for key in CAD_CONTAINER_KEYS:
        raw = container.get(key)
        if not raw:
            continue
        items = raw if isinstance(raw, list) else [raw]
        for item in items:
            if isinstance(item, str):
                asset_type = _normalize_cad_type(key)
                _append_resource(
                    collected,
                    seen,
                    url=item,
                    provider=provider,
                    description=key,
                    asset_type=asset_type,
                )
                continue
            if not isinstance(item, dict):
                continue
            url = (
                item.get("Url")
                or item.get("Value")
                or item.get("Link")
                or item.get("DownloadUrl")
            )
            if not url:
                continue
            description = (
                item.get("Description")
                or item.get("Title")
                or item.get("Name")
                or item.get("Type")
                or item.get("UrlType")
                or key
            )
            provider_name = item.get("Provider") or provider
            asset_type = _normalize_cad_type(" ".join([description or "", key]))
            _append_resource(
                collected,
                seen,
                url=url,
                provider=provider_name,
                description=description,
                asset_type=asset_type,
            )
    return collected


def _collect_external_library_resources(hit: Dict[str, Any], seen: set) -> List[CADResource]:
    resources: List[CADResource] = []
    libraries = hit.get("ExternalPartLibraries") or []
    if isinstance(libraries, dict):
        libraries = [libraries]
    for lib in libraries:
        if not isinstance(lib, dict):
            continue
        provider = lib.get("Provider") or lib.get("Name") or "external"
        description = lib.get("Description") or provider
        for field, asset_type in (
            ("SymbolUrl", "symbol"),
            ("SchematicSymbolUrl", "symbol"),
            ("FootprintUrl", "footprint"),
            ("PcbFootprintUrl", "footprint"),
            ("LandPatternUrl", "footprint"),
            ("StepUrl", "step"),
            ("ModelUrl", "step"),
            ("ThreeDModelUrl", "step"),
            ("LandingUrl", "other"),
            ("Url", "other"),
        ):
            url = lib.get(field)
            if url:
                _append_resource(
                    resources,
                    seen,
                    url=url,
                    provider=provider,
                    description=description or field,
                    asset_type=asset_type,
                )
    return resources


def _collect_cad_resources(hit: Dict[str, Any], details: Optional[Dict[str, Any]]) -> List[CADResource]:
    resources: List[CADResource] = []
    seen: set = set()
    hit_dict = hit or {}
    details_dict = details or {}

    for container, provider in (
        (hit_dict, "digikey"),
        (details_dict, "digikey"),
        (details_dict.get("Product") if isinstance(details_dict, dict) else None, "digikey"),
    ):
        if isinstance(container, dict):
            resources.extend(_collect_resources_from_container(container, provider=provider, seen=seen))

    resources.extend(_collect_external_library_resources(hit_dict, seen))

    return resources


def _part_identifier(row: Dict[str, Any]) -> str:
    for key in ("dk_part_number", "mpn", "query"):
        value = (row.get(key) or "").strip()
        if value:
            return value
    return "part"


def _parse_filename_from_headers(headers: Dict[str, str]) -> Optional[str]:
    content_disposition = headers.get("content-disposition") or headers.get("Content-Disposition")
    if not content_disposition:
        return None
    match = re.search(r"filename\*=UTF-8''(?P<filename>[^;]+)", content_disposition)
    if match:
        return _sanitize_filename(match.group("filename"))
    match = re.search(r'filename="?([^";]+)"?', content_disposition)
    if match:
        return _sanitize_filename(match.group(1))
    return None


def _guess_filename_from_url(url: str) -> Optional[str]:
    parsed = urlparse(url)
    candidate = os.path.basename(parsed.path)
    return _sanitize_filename(candidate) if candidate else None


def _download_cad_asset(
    session: requests.Session,
    url: str,
    dest_dir: Path,
    filename_hint: str,
) -> Optional[str]:
    try:
        response = session.get(url, stream=True, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
    except Exception:
        return None
    filename = _parse_filename_from_headers(response.headers) or _guess_filename_from_url(url)
    if not filename:
        filename = f"{_sanitize_filename(filename_hint)}.bin"
    dest_dir.mkdir(parents=True, exist_ok=True)
    output_path = dest_dir / filename
    try:
        with open(output_path, "wb") as handle:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    handle.write(chunk)
    except Exception:
        return None
    return str(output_path)


def _resource_location(resources: List[CADResource], asset_type: str) -> str:
    for resource in resources:
        if resource.asset_type == asset_type:
            return resource.local_path or resource.url or ""
    return ""


def _provider_matches(name: Optional[str], filters: Optional[set[str]]) -> bool:
    if not filters:
        return True
    normalized = (name or "").lower()
    if "any" in filters:
        return True
    if normalized in filters:
        return True
    return any(normalized.startswith(prefix) for prefix in filters)


# ----------------------- Core OAuth -----------------------

def _get_access_token(client_id: str, client_secret: str, scope: str = "productsearch") -> Tuple[str, int]:
    """Get OAuth2 client-credentials token. Returns (token, expiry_epoch)."""
    resp = requests.post(
        f"{BASE_AUTH}/connect/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": scope,
        },
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    tok = resp.json()
    return tok["access_token"], int(time.time()) + int(tok.get("expires_in", 3300))


def _headers(token: str, client_id: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "X-DIGIKEY-Client-Id": client_id,
        "Content-Type": "application/json",
    }


# ----------------------- API Calls -----------------------

def _keyword_search(
    session: requests.Session,
    base_api: str,
    token: str,
    client_id: str,
    query: str,
    limit: int,
    require_stock: bool,
) -> Dict[str, Any]:
    payload = {
        "Keywords": query,
        "RecordCount": limit,
        "Filters": {
            "HasQuantityAvailable": bool(require_stock),
            "ExcludeNonStock": bool(require_stock),
        },
    }
    resp = session.post(
        f"{base_api}/products/keywordsearch",
        headers=_headers(token, client_id),
        json=payload,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _product_details(
    session: requests.Session,
    base_api: str,
    token: str,
    client_id: str,
    product_number: str,
) -> Optional[Dict[str, Any]]:
    encoded = quote(product_number, safe="")
    resp = session.get(
        f"{base_api}/search/{encoded}/productdetails",
        headers=_headers(token, client_id),
        timeout=DEFAULT_TIMEOUT,
    )
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def _pick_best_hit(result_json: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    products = (result_json or {}).get("Products", []) or []
    if not products:
        return None
    stocked = [p for p in products if (p or {}).get("QuantityAvailable", 0) > 0]
    return stocked[0] if stocked else products[0]


def _price_at(pricing: List[Dict[str, Any]], qty_break: int) -> str:
    for brk in pricing or []:
        if brk.get("BreakQuantity") == qty_break:
            return str(brk.get("UnitPrice", ""))
    best = None
    for brk in pricing or []:
        bq = brk.get("BreakQuantity")
        if isinstance(bq, int) and bq <= qty_break:
            if best is None or bq > best.get("BreakQuantity", -1):
                best = brk
    return str(best.get("UnitPrice", "")) if best else ""


def _empty_row(query: str, error: Optional[str] = None) -> Dict[str, Any]:
    raw: Dict[str, Any] = {}
    if error:
        raw["error"] = error
    return {
        "query": query,
        "dk_part_number": "",
        "mpn": "",
        "manufacturer": "",
        "qty_available": 0,
        "price_1": "",
        "price_10": "",
        "price_100": "",
        "product_url": "",
        "cad_symbol": "",
        "cad_footprint": "",
        "cad_step": "",
        "cad_resources": json.dumps([], ensure_ascii=False),
        "raw": raw,
    }


# ----------------------- Public Function -----------------------

def fetch_digikey_parts(
    queries: Iterable[str],
    *,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    limit: int = DEFAULT_LIMIT,
    require_stock: bool = True,
    use_sandbox: Optional[bool] = None,
    fetch_cad: bool = False,
    cad_download: bool = False,
    cad_output_dir: Optional[str] = None,
    cad_providers: Optional[Sequence[str]] = None,
) -> List[Dict[str, Any]]:
    """
    Query Digi-Key Product Information v4 for a list of queries (MPN, DKPN or keywords).

    Returns a list of dicts with:
      query, dk_part_number, mpn, manufacturer, qty_available,
      price_1, price_10, price_100, product_url (if available),
      cad_symbol, cad_footprint, cad_step, cad_resources (JSON string), raw (json)
    """
    client_id = client_id or os.getenv("DK_CLIENT_ID", "").strip()
    client_secret = client_secret or os.getenv("DK_CLIENT_SECRET", "").strip()
    if not client_id or not client_secret:
        raise RuntimeError("Missing Digi-Key credentials. Set DK_CLIENT_ID and DK_CLIENT_SECRET.")

    if use_sandbox is None:
        use_sandbox = os.getenv("DK_USE_SANDBOX", "false").lower() in ("1", "true", "yes", "y")

    base_api = BASE_API_SANDBOX if use_sandbox else BASE_API_PROD

    fetch_cad = bool(fetch_cad or cad_download)
    cad_root: Optional[Path] = None
    cad_provider_filter: Optional[set[str]] = None
    if cad_providers:
        cad_provider_filter = {p.lower() for p in cad_providers if p}
    if cad_download:
        cad_root = Path(cad_output_dir or "cad_cache")

    token, token_exp = _get_access_token(client_id, client_secret)

    out_rows: List[Dict[str, Any]] = []

    with requests.Session() as session:
        for q in queries:
            query = (q or "").strip()
            if not query:
                continue

            row: Optional[Dict[str, Any]] = None
            attempts = 0

            while attempts < MAX_RETRIES:
                if time.time() > token_exp - 30:
                    token, token_exp = _get_access_token(client_id, client_secret)

                try:
                    search_result = _keyword_search(
                        session,
                        base_api,
                        token,
                        client_id,
                        query,
                        limit,
                        require_stock,
                    )
                    hit = _pick_best_hit(search_result)
                    if not hit:
                        row = _empty_row(query)
                        break

                    dkpn = hit.get("DigiKeyPartNumber", "")
                    mpn = hit.get("ManufacturerPartNumber", "")
                    manufacturer = (hit.get("Manufacturer") or {}).get("Value", "")
                    qty_available = int(hit.get("QuantityAvailable", 0) or 0)
                    product_url = hit.get("ProductUrl", "") or hit.get("ProductDetailUrl", "")

                    details_target = dkpn or mpn
                    pricing: List[Dict[str, Any]] = []
                    details: Dict[str, Any] = {}
                    if details_target:
                        details = _product_details(session, base_api, token, client_id, details_target) or {}
                        product = details.get("Product", details)
                        pricing = product.get("StandardPricing") or details.get("StandardPricing") or []

                    row = {
                        "query": query,
                        "dk_part_number": dkpn,
                        "mpn": mpn,
                        "manufacturer": manufacturer,
                        "qty_available": qty_available,
                        "price_1": _price_at(pricing, 1),
                        "price_10": _price_at(pricing, 10),
                        "price_100": _price_at(pricing, 100),
                        "product_url": product_url,
                        "cad_symbol": "",
                        "cad_footprint": "",
                        "cad_step": "",
                        "cad_resources": json.dumps([], ensure_ascii=False),
                        "raw": hit,
                    }

                    if fetch_cad:
                        cad_resources = _collect_cad_resources(hit, details)
                        if cad_provider_filter:
                            cad_resources = [
                                resource
                                for resource in cad_resources
                                if _provider_matches(resource.provider, cad_provider_filter)
                            ]

                        if cad_download and cad_root is not None and cad_resources:
                            part_slug = _sanitize_filename(_part_identifier(row))
                            part_dir = cad_root / part_slug
                            downloaded_types: set[str] = set()
                            for resource in cad_resources:
                                asset_type = resource.asset_type
                                if asset_type not in CAD_PRIMARY_TYPES:
                                    continue
                                if asset_type in downloaded_types:
                                    continue
                                saved_path = _download_cad_asset(
                                    session,
                                    resource.url,
                                    part_dir,
                                    f"{asset_type}_{resource.provider or 'cad'}",
                                )
                                if saved_path:
                                    resource.local_path = saved_path
                                    downloaded_types.add(asset_type)

                        if cad_resources:
                            row["cad_symbol"] = _resource_location(cad_resources, "symbol")
                            row["cad_footprint"] = _resource_location(cad_resources, "footprint")
                            row["cad_step"] = _resource_location(cad_resources, "step")
                            row["cad_resources"] = json.dumps(
                                [
                                    {
                                        "provider": res.provider,
                                        "asset_type": res.asset_type,
                                        "url": res.url,
                                        "description": res.description,
                                        "local_path": res.local_path,
                                    }
                                    for res in cad_resources
                                ],
                                ensure_ascii=False,
                            )

                    break

                except requests.HTTPError as exc:
                    response = exc.response
                    status = response.status_code if response is not None else None

                    if status in {401, 403}:
                        token, token_exp = _get_access_token(client_id, client_secret)
                        attempts += 1
                        continue

                    if status == 429:
                        retry_after = 5.0
                        if response is not None:
                            header = response.headers.get("Retry-After")
                            try:
                                retry_after = float(header)
                            except (TypeError, ValueError):
                                pass
                        time.sleep(max(1.0, min(retry_after, 30.0)))
                        attempts += 1
                        continue

                    row = _empty_row(query, f"HTTP {status} {exc}")
                    break

                except Exception as exc:  # pragma: no cover - best effort logging
                    row = _empty_row(query, str(exc))
                    break

            if row is None:
                row = _empty_row(query, "Exceeded retry attempts")

            out_rows.append(row)

    return out_rows


# ----------------------- CSV Helper -----------------------

def write_csv(rows: List[Dict[str, Any]], csv_path: str) -> None:
    fieldnames = [
        "query",
        "dk_part_number",
        "mpn",
        "manufacturer",
        "qty_available",
        "price_1",
        "price_10",
        "price_100",
        "product_url",
        "cad_symbol",
        "cad_footprint",
        "cad_step",
        "cad_resources",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


# ----------------------- CLI -----------------------

def _read_queries_from_file(path: str) -> List[str]:
    queries: List[str] = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                queries.append(stripped)
    return queries


def main() -> None:
    parser = argparse.ArgumentParser(description="Digi-Key lookup for FabOps (Product Info v4).")
    parser.add_argument("--in", dest="infile", help="Path to txt file with queries (one per line).")
    parser.add_argument("--queries", nargs="*", help="Queries as CLI args (MPN/DKPN/keywords).")
    parser.add_argument("--out", default="digikey_quote.csv", help="Output CSV path.")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Max records per keyword search.")
    parser.add_argument("--no-stock", action="store_true", help="Include parts without on-hand stock.")
    parser.add_argument("--sandbox", action="store_true", help="Use Digi-Key Sandbox API.")
    parser.add_argument("--cad", action="store_true", help="Collect CAD resource metadata for each part.")
    parser.add_argument(
        "--cad-download",
        action="store_true",
        help="Download CAD assets to --cad-dir (implies --cad).",
    )
    parser.add_argument("--cad-dir", default="cad_cache", help="Directory for downloaded CAD assets.")
    parser.add_argument(
        "--cad-providers",
        nargs="*",
        help="Limit CAD providers (case-insensitive). Example: --cad-providers digikey samacsys",
    )
    args = parser.parse_args()

    queries: List[str] = []
    if args.infile:
        queries.extend(_read_queries_from_file(args.infile))
    if args.queries:
        queries.extend(args.queries)
    if not queries:
        print("No queries provided. Use --in or --queries.")
        return

    rows = fetch_digikey_parts(
        queries,
        limit=args.limit,
        require_stock=not args.no_stock,
        use_sandbox=args.sandbox
        or (os.getenv("DK_USE_SANDBOX", "false").lower() in ("1", "true", "yes", "y")),
        fetch_cad=args.cad or args.cad_download,
        cad_download=args.cad_download,
        cad_output_dir=args.cad_dir,
        cad_providers=args.cad_providers,
    )
    write_csv(rows, args.out)
    print(f"Wrote {args.out} with {len(rows)} rows.")


if __name__ == "__main__":
    main()
