## What is **uv** (in plain terms)?

**uv** is a *fast, all‑in‑one* Python package & project manager written in Rust. It replaces or wraps what you’d usually do with `pip`, `pip-tools`, `virtualenv`, `pipx`, `poetry/rye` (project management), `pyenv` (Python installs), and even `twine` (publishing)—with one consistent CLI. It’s designed to be **10–100× faster**, uses a global cache, manages environments, can install and switch Python versions, and provides a *universal lockfile* for reproducible builds across platforms. ([Astral Docs][1])

Key properties you’ll feel immediately:

* **Speed** and caching → less waiting, fewer rebuilds. ([Astral Docs][2])
* **One tool for everything** → venvs, installs, lockfiles, tools (like `ruff`, `black`) via `uvx`, Python versions, builds, publish. ([Astral Docs][1])
* **Universal lockfile (`uv.lock`)** → one lock works on macOS, Linux, Windows; reproducible (same set of packages) everywhere. ([Astral Docs][3])

---

## Install uv

Pick one:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You can also install via pip or Homebrew, but the above is the official installer. ([Astral Docs][1])

---

## Two common ways to use uv

### A) **Keep your current `requirements.txt` workflow (fast drop‑in)**

This gives you immediate speedups with minimal change.

```bash
# 1) Create a venv (defaults to ./.venv). uv prefers venvs by default.
uv venv

# 2) Install from a requirements file (like pip install -r)
uv pip install -r requirements.txt

# 3) Exact sync (removes extras not in the file) — use in CI
uv pip sync requirements.txt
```

Notes:

* **uv requires venvs by default**, which keeps your system Python clean. Activate if you want, or just use `uv run` (see below). ([Astral Docs][4])
* Prefer **`uv pip sync`** in CI to guarantee the environment *exactly* matches the file. ([Astral Docs][5])
* You can also **compile** deterministic requirements like `pip-compile`, including *universal* (cross‑platform) output:
  `uv pip compile --universal requirements.in -o requirements.txt`. ([Astral Docs][5])

---

### B) **Adopt uv’s project workflow (recommended for new apps/libs)**

This is similar to Poetry/Rye but faster and simpler.

```bash
# 1) Initialize a project
uv init my-app
cd my-app

# 2) Add dependencies (persists to pyproject.toml)
uv add fastapi "pydantic>=2"

# 3) Run commands in a managed, up-to-date env (no manual activate needed)
uv run -- python -V
uv run -- pytest
```

What happens:

* uv creates `pyproject.toml`, a `.venv` next to it, and a **`uv.lock`** universal lockfile. The lock & environment are kept in sync automatically when you run `uv run` or `uv sync`. Use `--locked` / `--frozen` if you need strictness in CI. ([Astral Docs][6])
* The project environment lives in `./.venv`. Avoid mutating it directly with `uv pip install`; prefer `uv add` so your project files stay the source of truth. ([Astral Docs][3])

If you ever need to export to other formats (e.g., to interop with existing pipelines):

```bash
# Export uv.lock to requirements.txt or PEP 751 pylock.toml
uv export -o requirements.txt
uv export -o pylock.toml
```

And yes, uv can install from **`pylock.toml`** and sync it, too. ([Astral Docs][7])

---

## Essential everyday commands (cheat sheet)

### Environments & running

```bash
uv venv                     # create .venv (optionally: uv venv --python 3.12)
uv run -- pytest -q         # run inside the project env, syncing/locking first
uv sync                     # just sync the env from uv.lock
uv sync --locked            # fail if lockfile isn't current (good for CI)
uv sync --no-dev            # install runtime deps only (skip dev group)
```

Locking & syncing behaviors and flags (automatic, `--locked`, `--frozen`, `--no-sync`) are documented here. ([Astral Docs][8])

### Managing dependencies (project-centric)

```bash
uv add "httpx>=0.27"        # add prod dep (writes to [project.dependencies])
uv add --dev pytest         # add dev-only dep ([dependency-groups], PEP 735)
uv remove httpx             # remove a dep
uv lock --upgrade           # upgrade everything in the lock
uv lock --upgrade-package httpx==0.28.0  # upgrade one package
uv tree                     # view the dependency tree
```

uv uses modern fields: `project.dependencies`, `project.optional-dependencies` (extras), and `dependency-groups` for dev/test tooling (PEP 735). The **dev group is installed by default** unless you opt out. ([Astral Docs][9])

### “pip-compatible” commands (low-friction adoption)

```bash
uv pip install -r requirements.txt     # like pip install -r
uv pip sync requirements.txt           # exact sync from a lock file
uv pip compile requirements.in -o requirements.txt
uv pip list / show / freeze / check / tree
```

This interface is **pip‑compatible in spirit** but doesn’t actually call pip; it’s uv’s own engine. ([Astral Docs][10])

### One-off tools (like `pipx run`)

```bash
uvx ruff@latest check .        # run a tool in a temp (ephemeral) env
uv tool install ruff           # install a tool persistently into PATH
uv tool upgrade --all
```

`uvx` is just an alias for `uv tool run`. If a tool needs your *project* (e.g., `pytest`, `mypy`), prefer `uv run` so it sees your project and venv. ([Astral Docs][11])

### Python versions (pyenv-like)

```bash
uv python list
uv python install 3.12.7       # install a specific CPython
uv python pin 3.12             # write .python-version for the project
uv run --python 3.11 -- python -V
uv python upgrade 3.12         # upgrade to latest 3.12.x (preview feature)
```

uv can discover, download, and manage CPython/PyPy; it can also add `python3.12` into your PATH if requested. ([Astral Docs][12])

### Caching (speed & hygiene)

```bash
uv cache dir
uv cache prune --ci            # keep built wheels, drop re-downloadable stuff
uv cache clean                 # nuke cache (or clean just one package)
```

Aggressive caching makes uv fast; these commands help when you need a reset. ([Astral Docs][2])

---

## Pip → uv mental model (quick mapping)

| What you do today        | uv (project‑first)                     | uv (pip‑compatible)                    | When to use                                                                                                             |
| ------------------------ | -------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `python -m venv .venv`   | `uv venv [--python X.Y]`               | —                                      | Create a venv quickly. ([Astral Docs][4])                                                                               |
| activate & run           | `uv run -- <cmd>`                      | —                                      | Runs with auto lock/sync, no manual activate. ([Astral Docs][6])                                                        |
| `pip install foo`        | `uv add foo`                           | `uv pip install foo`                   | Use `uv add` to **persist** deps in `pyproject.toml`; use `uv pip install` only for ad‑hoc installs. ([Astral Docs][9]) |
| `pip install -r req.txt` | —                                      | `uv pip install -r req.txt`            | Quick install from a file (non‑exact). ([Astral Docs][5])                                                               |
| `pip-compile`            | —                                      | `uv pip compile … -o requirements.txt` | Produce reproducible `requirements.txt`; add `--universal` for cross‑platform. ([Astral Docs][5])                       |
| `pipx run tool`          | `uv run --with tool …` (project aware) | `uvx tool`                             | Use `uv run` for tools that need your project (e.g., `pytest`); `uvx` for standalone tools. ([Astral Docs][11])         |
| `pyenv install 3.12.7`   | `uv python install 3.12.7`             | —                                      | Manage CPython/PyPy versions via uv. ([Astral Docs][12])                                                                |

---

## A 10‑minute hands‑on (from your current knowledge)

**Scenario:** Existing repo with `requirements.in` + `requirements.txt`

```bash
# create venv and install exactly what's locked
uv venv
uv pip sync requirements.txt

# later, bump a dependency and regenerate lock
uv pip compile --universal requirements.in -o requirements.txt
uv pip sync requirements.txt
```

**Scenario:** New service with a modern, persistent project config

```bash
uv init --app my-service           # app scaffold
cd my-service
uv add "fastapi>=0.111" uvicorn    # deps -> pyproject.toml
uv run -- uvicorn main:app --reload
# add dev tooling
uv add --dev pytest ruff
uv run -- pytest -q
```

Behind the scenes, uv produces/maintains `uv.lock`, keeps `./.venv` in sync, and can export to `requirements.txt`/`pylock.toml` when you need interop. ([Astral Docs][6])

---

## Extra tips for a backend/dev‑ops workflow

* **CI pattern** (fail fast if out-of-date):
  `uv sync --locked && uv run -- pytest -q`
  `--locked` asserts the lockfile matches `pyproject.toml`. ([Astral Docs][8])
* **Jupyter workflow**: Run Jupyter against your project env without manual wiring:
  `uv run --with jupyter jupyter lab` (and add `ipykernel` as a dev dep if you need a dedicated kernel). ([Astral Docs][13])
* **Docker**: Either copy the uv binary from official images or install in the image; then `uv sync --locked` during build for reproducible layers. ([Astral Docs][14])

---

## What’s different vs pip/venv (the “gotchas”)

* **Use `uv add` to persist** dependencies. `uv pip install` changes the env but **does not** update `pyproject.toml`/`uv.lock`. ([Astral Docs][3])
* **Universal lockfile**: `uv.lock` is uv‑specific and intended to be checked into VCS; export to `requirements.txt` or **PEP 751 `pylock.toml`** when you must interoperate. ([Astral Docs][3])
* **`uvx` vs `uv run`**: `uvx` runs tools in a *temporary* env; use `uv run` for project‑aware tools (pytest, mypy) so they see your code and deps. ([Astral Docs][11])

---

## A minimal `pyproject.toml` you’ll recognize

```toml
[project]
name = "my-app"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "fastapi>=0.111",
]

# optional “extras”
[project.optional-dependencies]
docs = ["mkdocs", "mkdocs-material"]

# dev/test groups (PEP 735)
[dependency-groups]
dev = ["pytest", "ruff"]

# uv-only dev source overrides live under tool.uv
[tool.uv]
# e.g., managed = false  # if you want to turn off auto sync/lock
```

Dev groups and extras behavior are first-class in uv and respected by `uv sync` flags. ([Astral Docs][9])

---

### Reference highlights to keep handy

* **Intro & highlights** (speed, scope, lockfile): ([Astral Docs][1])
* **Pip‑compatible commands** (`uv pip …`) & venv defaults: ([Astral Docs][10])
* **Lock & sync workflow** (auto lock/sync, `--locked`, `--frozen`): ([Astral Docs][8])
* **Universal lockfile & `pylock.toml`**: ([Astral Docs][3])
* **`uvx` and tool management**: ([Astral Docs][11])
* **Install Python versions**: ([Astral Docs][12])
* **Caching controls**: ([Astral Docs][2])
* **Project init variants** (`uv init --app`): ([Astral Docs][7])
* **Requirements compile/sync** (universal compile): ([Astral Docs][5])

---

[1]: https://docs.astral.sh/uv/ "uv"
[2]: https://docs.astral.sh/uv/concepts/cache/ "Caching | uv"
[3]: https://docs.astral.sh/uv/concepts/projects/layout/ "Structure and files | uv"
[4]: https://docs.astral.sh/uv/pip/environments/ "Using environments | uv"
[5]: https://docs.astral.sh/uv/pip/compile/ "Locking environments | uv"
[6]: https://docs.astral.sh/uv/guides/projects/ "Working on projects | uv"
[7]: https://docs.astral.sh/uv/reference/cli/ "Commands | uv"
[8]: https://docs.astral.sh/uv/concepts/projects/sync/ "Locking and syncing | uv"
[9]: https://docs.astral.sh/uv/concepts/projects/dependencies/ "Managing dependencies | uv"
[10]: https://docs.astral.sh/uv/pip/ "Index | uv"
[11]: https://docs.astral.sh/uv/guides/tools/ "Using tools | uv"
[12]: https://docs.astral.sh/uv/concepts/python-versions/ "Python versions | uv"
[13]: https://docs.astral.sh/uv/guides/integration/jupyter/ "Using uv with Jupyter | uv"
[14]: https://docs.astral.sh/uv/guides/integration/docker/ "Using uv in Docker | uv"
