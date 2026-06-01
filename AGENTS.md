# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **BN314 System Architecture (Assignment 2)** artifact generator for the **FreshBite Salads** case study. It is **not** a deployable web application: there are no HTTP services, databases, Docker Compose stacks, or committed test/lint configs.

### What runs here

| Script | Output |
|--------|--------|
| `draw_dfd.py`, `draw_dfd_v2.py`, `draw_dfd_v3.py` | PNG DFD diagrams under `output/` |
| `draw_class_v2.py`, `draw_class_v3.py` | PNG class diagrams under `output/` |
| `generate_drawio.py` | `output/FreshBite_DFD.drawio`, `output/FreshBite_ClassDiagram.drawio` |
| `create_document.py` | `output/BN314_A2_Q5_Q6_Answer.docx` (embeds `dfd_v3.png` and `class_v3.png`) |

Run generators from the repo root with `python3 <script>.py`. **`create_document.py` must run after** `draw_dfd_v3.py` and `draw_class_v3.py` because it embeds those PNGs.

### Dependencies

- **Python 3** (3.12+ tested)
- **pip packages:** `matplotlib`, `python-docx` (`draw_dfd_v2.py` also uses `numpy`, usually already present on the VM)

No environment variables or secrets are required.

### Lint / tests

There is no `requirements.txt`, `pyproject.toml`, pytest suite, or linter configuration in this repo. Validation is **regenerating outputs** and confirming files under `output/` update without errors.

### Gotchas

- Matplotlib uses the **Agg** backend (headless); no display server is needed.
- Scripts write to **absolute paths** under `/workspace/output/`. Keep the repo at `/workspace` in Cloud Agent VMs, or adjust paths if the workspace root differs.
- `draw_dfd.py` may emit harmless matplotlib `UserWarning` messages about circle `color` vs `edgecolor`; generation still succeeds.
