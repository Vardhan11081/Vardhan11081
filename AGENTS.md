# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is

BN314 Assignment 2 artifact generator for the **FreshBite Salads** case study. There is no web app, database, or long-running service—only batch Python scripts that write files under `output/`.

### Dependencies

- Python 3.12+ (stdlib + pip packages)
- `matplotlib` and `python-docx` (install via the VM update script or `pip3 install matplotlib python-docx`)
- `numpy` only if you run the legacy script `draw_dfd_v2.py`

### End-to-end pipeline (from repo root)

Run in this order; `create_document.py` requires `output/dfd_v3.png` and `output/class_v3.png`:

```bash
python3 draw_dfd_v3.py
python3 draw_class_v3.py
python3 generate_drawio.py   # optional; stdlib only
python3 create_document.py
```

### Lint / test

- No ESLint, Ruff, pytest, or CI config in the repo.
- Practical checks: `python3 -m py_compile *.py` and re-run the pipeline above, then confirm files under `output/` (especially `BN314_A2_Q5_Q6_Answer.docx`).

### Matplotlib

Diagram scripts set `matplotlib.use('Agg')` before importing `pyplot`, so a display server is not required in Cloud Agent VMs.

### Outputs

All generators write to `output/` with paths hardcoded in the scripts. Do not expect hot reload or a dev server.
