# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **Python batch pipeline** for BN314 Assignment 2 (FreshBite Salads diagrams and Word document). There are **no long-running services**, Docker compose stacks, or network ports.

### What runs here

| Step | Command | Output |
|------|---------|--------|
| DFD (v3) | `python3 draw_dfd_v3.py` | `output/dfd_v3.png` |
| Class diagram (v3) | `python3 draw_class_v3.py` | `output/class_v3.png` |
| Word document | `python3 create_document.py` | `output/BN314_A2_Q5_Q6_Answer.docx` |
| Draw.io XML (optional) | `python3 generate_drawio.py` | `output/FreshBite_*.drawio` |

Run diagram scripts **before** `create_document.py`; the document embeds `dfd_v3.png` and `class_v3.png`.

### Dependencies

Python 3 with **matplotlib** (Agg backend) and **python-docx**. Legacy scripts (`draw_dfd_v2.py`) also use **numpy**.

### Lint / tests

There is no project linter or test suite. A quick sanity check is `python3 -m py_compile` on the `.py` files, then run the pipeline above and confirm files under `output/`.

### Gotchas

- Matplotlib must use the non-interactive backend (`Agg`); scripts set this at import time.
- `README.md` at the repo root is a GitHub profile readme, not project setup docs; use this file and the script docstrings instead.
