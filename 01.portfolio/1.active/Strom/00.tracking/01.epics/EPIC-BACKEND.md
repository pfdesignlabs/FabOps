# EPIC — Backend Integration

## Doel
Een betrouwbare data- en automatiseringspijplijn voor Strom neerzetten via MQTT, Telegraf, InfluxDB en Home Assistant.

## Doelen
- Presence-events via MQTT binnenhalen
- Dashboards voor sensortelemetrie
- Basisautomatiseringen in Home Assistant
- Betrouwbare logging end-to-end

## Scope
- MQTT-topics
- Telegraf-collectors
- InfluxDB-schema
- Grafana-dashboards

## Buiten scope
- Firmware-logica op het device zelf

## Kritieke prestatie-indicatoren
- Presence-eventverwerking < 200 ms
- Dashboard-beschikbaarheid > 99%
- Geen dropped messages onder WiFi-stresstest

## Links
- ../02.stories/
- ../../08.validation/README.md
