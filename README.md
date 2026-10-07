# mac_in_orbit

> Recover the **secret key** from **mac** (message authentication code).

Template repository for bootstrapping new GitHub projects with consistent structure, documentation, and workflow conventions.

## Table of Contents

- [Overview](#overview)
- [Test The Project](#test-the-project)
- [Included Files](#included-files)
- [Project Structure](#project-structure)
- [Conventions](#conventions)
- [Roadmap Seed](#roadmap-seed)
- [License](#license)

## Overview

This repository is intentionally generic. Replace placeholders and keep only the sections/files that match your generated project.

### Goals

- Provide a clean baseline for new repositories.
- Keep documentation and release tracking ready from day one.
- Preserve lightweight defaults with minimal tooling assumptions.

## Test The Project

1. On GitHub, click **Use this template**.
2. Create a new repository from this template.
3. Clone the generated repository:

```bash
git clone https://github.com/fevunge/mac_in_orbit.git
cd mac_in_orbit

python mac.py
```

## Included Files

| File | Purpose |
|---|---|
| `mac.py` |  the reference implementation of the MAC. Put your candidate into KEY_CANDIDATE
and run the file. |
| `intercepted-pair.txt` | command and tag, ready to copy. |


## Project Structure

```text
 .
├──  __pycache__
│   └──  mac.cpython-314.pyc
├──  assets
│   └── 󰕙 MAC.svg
├──  intercepted-pair.txt
├──  mac.py
└── 󰂺 README.md
```

## Conventions

- Commit style: [Conventional Commits](https://www.conventionalcommits.org/).
- Changelog style: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
- Versioning style: [Semantic Versioning](https://semver.org/).
- Keep template docs abstract and reusable; avoid product-specific business logic.

## Roadmap Seed

- [ ] Add `CONTRIBUTING.md` with branch and PR guidelines.
- [ ] Add `LICENSE` with selected template default.
- [ ] Add reusable `.github/workflows/` CI pipelines.
- [ ] Add portable `Makefile` targets (`all`, `build`, `test`, `lint`, `clean`, `fclean`, `re`, `install`).

## License

{{LICENSE_NAME}} (replace this section with the final license reference for generated projects).

