## 1) Create project & scaffold

```bash
mkdir uv-official-demo
cd uv-official-demo
uv init --app
```

This creates `pyproject.toml`, `src/uv_official_demo/__init__.py`, etc.

---

## 2) Add your script

Create `main.py` in project root:

```python
# main.py
import requests

def main():
    r = requests.get("https://api.github.com")
    print("Status:", r.status_code)
    print("Some keys:", list(r.json().keys())[:5])

if __name__ == "__main__":
    main()
```

---

## 3) Pin libraries (versions) in `pyproject.toml`

Open `pyproject.toml` and set explicit versions. Example (good with Python 3.12.7):

```toml
[project]
name = "uv-official-demo"
version = "0.1.0"
requires-python = ">=3.12"
# Runtime deps (used or not, all pinned):
dependencies = [
  "requests==2.32.3",
  "httpx==0.27.2",
  "pydantic==2.9.2",
  "numpy==2.1.2",
]

# Optional: dev/test tools (PEP 735 groups)
[dependency-groups]
dev = [
  "pytest==8.3.3",
  "ruff==0.6.9",
]
```

> Tip: Instead of editing TOML manually, you could run `uv add requests==2.32.3 httpx==0.27.2 ...` and `uv add --dev pytest==8.3.3 ruff==0.6.9`. Both approaches are valid; **editing + `uv sync`** is nice when you want explicit control.

---

## 4) Install exactly what’s declared (sync + lock)

```bash
uv sync
```

* Resolves deps → writes/updates `uv.lock` (universal lockfile).
* Installs everything into `./.venv`.

If you want to skip dev tools: `uv sync --no-dev`.

---

## 5) Run the program (no manual activate needed)

```bash
uv run -- python main.py
```

That’s it—`uv run` ensures the env matches your lock, then runs the script.

---

### Useful variations (short)

* Add a new pinned dep later:

  ```bash
  uv add "rich==13.9.2"
  uv run -- python -c "import rich; print(rich.__version__)"
  ```
* Upgrade the lock in place (all deps):

  ```bash
  uv lock --upgrade
  uv sync
  ```
* Upgrade just one package:

  ```bash
  uv lock --upgrade-package httpx==0.28.0
  uv sync
  ```
* Export to requirements.txt (for Docker or CI that expects it):

  ```bash
  uv export -o requirements.txt
  ```

---

### Mental model (quick)

* **Declare** in `pyproject.toml` (source of truth).
* **Lock & install** with `uv sync` (reproducible).
* **Run** with`uv run` (no activate, auto-consistent env).

---