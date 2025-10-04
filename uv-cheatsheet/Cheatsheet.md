## 🧠 1. Dependency Upgrades & Lockfile Management

Once you have a `pyproject.toml` and `uv.lock`, you’ll sometimes want to **upgrade** dependencies.

| Task                                        | Command                                      | Description                                                                          |
| ------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------ |
| Upgrade all deps to latest allowed versions | `uv lock --upgrade`                          | Regenerates `uv.lock` with latest versions based on constraints in `pyproject.toml`. |
| Upgrade one package                         | `uv lock --upgrade-package requests==2.33.0` | Updates only that library.                                                           |
| Regenerate env from lock                    | `uv sync`                                    | Ensures `.venv` exactly matches `uv.lock`.                                           |
| Freeze (no network, use lock only)          | `uv sync --locked`                           | Safe for CI/CD reproducibility.                                                      |

---

## ⚙️ 2. Environment / Tool Utilities

| Command                   | Description                                                           |
| ------------------------- | --------------------------------------------------------------------- |
| `uv venv`                 | Creates `.venv` automatically (respects `.python-version` if pinned). |
| `uv run -- python app.py` | Runs inside the managed environment.                                  |
| `uv tree`                 | Shows dependency tree.                                                |
| `uv cache dir`            | Shows global cache directory (shared across projects).                |
| `uv cache prune --ci`     | Cleans unnecessary files but keeps built wheels.                      |
| `uv cache clean`          | Clears everything.                                                    |

---

## 🧰 3. Tool Management (like pipx)

uv can install and run **CLI tools** globally — without polluting your venvs.

| Command                 | Description                                        |
| ----------------------- | -------------------------------------------------- |
| `uvx ruff@latest`       | Runs a tool temporarily (ephemeral env).           |
| `uv tool install black` | Installs tool globally into uv’s managed tool env. |
| `uv tool list`          | Lists installed tools.                             |
| `uv tool upgrade --all` | Upgrades all installed tools.                      |

This replaces `pipx`, and is super useful for dev tools (formatters, linters, etc.).

---

## 🧩 4. Python Version Management

| Command                             | Description                                              |
| ----------------------------------- | -------------------------------------------------------- |
| `uv python list`                    | Shows installed Python versions.                         |
| `uv python install 3.12.7`          | Installs that Python version.                            |
| `uv python pin 3.12`                | Pins project to that version (writes `.python-version`). |
| `uv run --python 3.11 -- python -V` | Run using a different version (temporarily).             |

This replaces `pyenv` or `asdf` for Python management.

---

## 📦 5. Exporting for Docker or CI/CD

If your CI/CD or Docker build expects `requirements.txt`, you can export:

```bash
uv export -o requirements.txt
```

Then inside Docker:

```dockerfile
RUN uv pip install -r requirements.txt
```

Or, for stricter builds:

```bash
uv sync --locked
```

(which guarantees the env matches your lock file).

---

## 🧾 6. Universal Lockfile & pylock.toml

uv’s `uv.lock` can be shared safely across OSes.
You can also export a PEP 751 compliant lockfile:

```bash
uv export -o pylock.toml
```

Then later recreate exactly the same env:

```bash
uv sync --from pylock.toml
```

---

## 🧪 7. Quick Testing & Dev Commands

| Use case                 | Command                        |
| ------------------------ | ------------------------------ |
| Run tests in project env | `uv run -- pytest`             |
| Skip dev deps (CI)       | `uv sync --no-dev`             |
| Add testing tools        | `uv add --dev pytest coverage` |
| Lint/format check        | `uv run -- ruff check .`       |

---


### Setup & Environments

| Command           | Key flags (meaning)                                                               | What it does                                                               | When to use                                         |
| ----------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------- |
| `uv venv`         | `--python 3.12` (choose interpreter), `PATH` (custom folder like `uv venv .venv`) | Creates a virtual environment in the current folder (defaults to `.venv`). | Start a fresh, isolated env for a project.          |
| `uv venv myenv`   | *(no flags)*                                                                      | Creates a venv named `myenv/`.                                             | Ad-hoc env without `pyproject.toml`.                |
| `uv run -- <cmd>` | `--python 3.11` (temporary Python), `--with PKG` (auto-install tool for run)      | Runs any command inside the managed env, ensuring deps are in sync first.  | Avoid manual `activate`; consistent runs in dev/CI. |

---

### Project Init & Metadata

| Command   | Key flags (meaning)                                     | What it does                                                                  | When to use                               |
| --------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------- |
| `uv init` | `--app` (scaffold app layout), `--lib` (library layout) | Initializes a project with `pyproject.toml`, source layout, and basic config. | New project; adopt the official workflow. |

---

### Dependencies (Project-first)

| Command           | Key flags (meaning)                                               | What it does                                                      | When to use                            |
| ----------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------- |
| `uv add PKG==X.Y` | `--dev` (dev-only group), `--extra name` (optional feature group) | Adds a dependency to `pyproject.toml` and updates the lock + env. | Persist and version your dependencies. |
| `uv remove PKG`   | *(no flags)*                                                      | Removes a dependency from `pyproject.toml` and the env.           | Cleanup unused packages.               |
| `uv tree`         | `--all` (show full transitive tree)                               | Displays dependency graph.                                        | Inspect why something is installed.    |

---

### Locking & Syncing (Reproducible installs)

| Command   | Key flags (meaning)                                                                                                                      | What it does                                                                      | When to use                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `uv sync` | `--locked` (fail if lock is stale), `--frozen` (don’t write lock), `--no-dev` (skip dev group), `--extra name` (include optional extras) | Installs to match `uv.lock`/`pyproject.toml`, ensuring env matches declared deps. | Standard install; CI uses `--locked` for strict reproducibility. |
| `uv lock` | `--upgrade` (bump all), `--upgrade-package PKG==X.Y` (bump one), `--prerelease` (allow pre-releases)                                     | (Re)solves and writes `uv.lock` without installing.                               | Adjust locked versions before syncing.                           |

---

### Pip-compatible (Low friction / Ad-hoc)

| Command                                              | Key flags (meaning)                                             | What it does                                                          | When to use                               |
| ---------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------- |
| `uv pip install PKG`                                 | `-r requirements.txt` (from file), `--pre` (allow pre-releases) | Installs into the **current env** (does not update `pyproject.toml`). | Quick tests or legacy workflows.          |
| `uv pip sync requirements.txt`                       | *(no flags)*                                                    | Makes env **exactly** match the file (removes extras).                | Deterministic CI with requirements files. |
| `uv pip compile requirements.in -o requirements.txt` | `--universal` (cross-OS pins), `--upgrade/--upgrade-package`    | Compiles pinned `requirements.txt` from high-level `.in`.             | Maintain classic reqs with precise pins.  |

---

### Running Apps & Tools

| Command                    | Key flags (meaning)                     | What it does                                                 | When to use                                  |
| -------------------------- | --------------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| `uv run -- python main.py` | `--with jupyter` (grab tool on-the-fly) | Executes Python using the project env; auto-syncs if needed. | Daily development runs.                      |
| `uvx TOOL@version args…`   | *(alias for `uv tool run`)*             | Runs a tool in an ephemeral (temporary) env.                 | One-off tooling (like `ruff`, `httpie`).     |
| `uv tool install TOOL`     | `--force` (overwrite), `--version X.Y`  | Installs a CLI tool into a persistent tool env on your PATH. | Replace `pipx` for globally available tools. |
| `uv tool upgrade --all`    | *(no flags)*                            | Upgrades all installed tools.                                | Keep global tools current.                   |

---

### Python Versions (Interpreter management)

| Command                         | Key flags (meaning) | What it does                                                           | When to use                               |
| ------------------------------- | ------------------- | ---------------------------------------------------------------------- | ----------------------------------------- |
| `uv python list`                | *(no flags)*        | Lists available/installed Python versions.                             | Audit interpreters on your system.        |
| `uv python install 3.12.7`      | *(no flags)*        | Downloads and installs the specified Python.                           | Ensure consistent Python across machines. |
| `uv python pin 3.12`            | *(no flags)*        | Writes `.python-version` for the project.                              | Enforce a project-wide Python version.    |
| `uv run --python 3.11 -- <cmd>` | *(no flags)*        | Run a command with a specific Python without changing the project pin. | Test across versions quickly.             |

---

### Exporting (Interop for Docker/CI)

| Command                         | Key flags (meaning)                                               | What it does                                                         | When to use                               |
| ------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------- |
| `uv export -o requirements.txt` | `--no-hashes` (omit hashes), `--format pip` (explicit pip format) | Exports deps from `uv.lock`/`pyproject.toml` to a requirements file. | Use in Dockerfiles or legacy CI.          |
| `uv export -o pylock.toml`      | *(PEP 751 lock)*                                                  | Exports a standards-based lockfile.                                  | Share precise env across platforms/tools. |
| `uv sync --from pylock.toml`    | *(no flags)*                                                      | Installs from a PEP 751 lockfile.                                    | Recreate exact envs anywhere.             |

---

### Cache & Hygiene (Speed & space)

| Command               | Key flags (meaning)                        | What it does                              | When to use                                 |
| --------------------- | ------------------------------------------ | ----------------------------------------- | ------------------------------------------- |
| `uv cache dir`        | *(no flags)*                               | Prints the location of uv’s global cache. | Inspect cache for troubleshooting.          |
| `uv cache prune --ci` | *(keeps wheels, drops re-fetchable items)* | Cleans cache conservatively for CI.       | Speed + smaller caches in pipelines.        |
| `uv cache clean`      | *(no flags)*                               | Clears cache entirely.                    | Fully reset when space or build issues hit. |

---

### Inspection & Troubleshooting

| Command           | Key flags (meaning)         | What it does                                 | When to use                     |
| ----------------- | --------------------------- | -------------------------------------------- | ------------------------------- |
| `uv pip list`     | `--outdated` (show updates) | Lists installed packages in the env.         | Quick audit of versions.        |
| `uv pip show PKG` | *(no flags)*                | Shows package metadata.                      | Inspect package origins/files.  |
| `uv pip check`    | *(no flags)*                | Verifies dependency consistency (conflicts). | Sanity check after big changes. |

---

### Practical combos (snippet recipes)

* **Strict CI install**
  `uv sync --locked && uv run -- pytest -q`
  *Ensures lock is current, then runs tests.*

* **Upgrade one dep and run**
  `uv lock --upgrade-package httpx==0.28.0 && uv sync && uv run -- pytest -q`

* **Run a tool without polluting your project**
  `uvx ruff@latest check .`

* **Docker-friendly export**
  `uv export -o requirements.txt` → in Docker: `RUN uv pip install -r requirements.txt`

---

