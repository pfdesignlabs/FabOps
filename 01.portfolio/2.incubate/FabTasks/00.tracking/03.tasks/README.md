# 03.tasks — Executable Work Items

Tasks are the atomic units of execution. They live inside this folder,
organised in a way that makes sense for you (per domain, per story, etc.).

Conventions:

- One directory per story, or per domain + story ID
- Inside that directory: one or more task files
- Task IDs: `FT-T-XXXX` where `XXXX` is a zero-padded integer

Each task file should cover:

- Parent story
- Status (todo / doing / review / done)
- Owner
- Sprint
- Definition of done
- Evidence links (commits, PRs, artifacts)

Tasks should be small enough to complete in a focused block of work.
