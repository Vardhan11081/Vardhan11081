# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is

Single flat **Python 3** project (no monorepo, no web server, no Docker). Scripts generate **FreshBite Salads** BN314 assignment artifacts: matplotlib PNG diagrams, optional draw.io XML, and a Word document under `/workspace/output/`.

### Dependencies

Install with pip (no `requirements.txt` in repo):

- **Required:** `matplotlib`, `python-docx`
- **Optional:** `numpy` (only for legacy `draw_dfd_v2.py`)

### Primary pipeline (end-to-end)

Run from `/workspace` in this order (document embeds v3 PNGs):

```bash
python3 draw_dfd_v3.py
python3 draw_class_v3.py
python3 create_document.py
```

Optional draw.io exports (stdlib only):

```bash
python3 generate_drawio.py
```

### Lint / test

- No configured linter or test suite.
- Syntax check: `python3 -m py_compile /workspace/*.py`
- Smoke test: run the primary pipeline above and confirm files under `output/` update (especially `dfd_v3.png`, `class_v3.png`, `BN314_A2_Q5_Q6_Answer.docx`).

### Paths

Scripts hardcode absolute paths under `/workspace/output/`. Run from a checkout at `/workspace` or adjust paths before running.

### Services

Nothing to start—no API, database, or dev server. “Running the app” means executing the generation scripts.
