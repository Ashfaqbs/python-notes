# 🧰 Python Tooling Command Cheat Sheet

## 🧪 `pip` – Python Package Installer

```bash
pip install package-name         # Install a package
pip uninstall package-name       # Uninstall a package
pip list                         # List installed packages
pip show package-name            # Show package details
pip freeze                       # Output installed packages
pip freeze > requirements.txt    # Save environment
pip install -r requirements.txt  # Install from requirements.txt
```

---

## ⚙️ `pipx` – Run CLI Tools in Isolated Environments

```bash
pipx install tool-name           # Install tool globally (e.g., black, uvicorn)
pipx list                        # List installed tools
pipx upgrade tool-name           # Upgrade tool
pipx uninstall tool-name         # Uninstall tool
```

> 🧠 Great for CLI tools that shouldn’t pollute your global or virtual env.

---

## 📦 `poetry` – Dependency & Project Manager

```bash
poetry new my-project            # Create new project
poetry init                      # Set up pyproject.toml
poetry install                   # Install dependencies
poetry add package-name          # Add dependency
poetry remove package-name       # Remove dependency
poetry update                    # Update all dependencies
poetry shell                     # Enter venv shell
poetry run python script.py      # Run script in poetry env
```

---

## ⚡ `uv` – Fast Package Installer (pip alternative)

```bash
uv pip install package-name      # Fast install
uv pip uninstall package-name    # Fast uninstall
uv pip list                      # List packages
uv venv create .venv             # Create virtual environment
uv venv exec python script.py    # Run script in env
```

> ⚡ Very fast, modern, and dependency-resolving tool.

---

## 🐍 `python` – Python CLI & Virtual Environments

```bash
python                           # Start REPL
python script.py                 # Run script
python --version                 # Show Python version
python -m venv .venv             # Create virtual env
source .venv/bin/activate        # Activate (macOS/Linux)
.venv\Scripts\activate           # Activate (Windows)
deactivate                       # Exit virtual env
```

---

## 🧪 `conda` – Environment & Package Manager

```bash
conda create -n myenv python=3.11      # Create new env
conda activate myenv                   # Activate env
conda deactivate                       # Deactivate env
conda install package-name             # Install a package
conda remove package-name              # Remove package
conda list                             # List installed packages
conda env export > env.yml             # Export env config
conda env create -f env.yml            # Create env from YAML
conda info --envs                      # List all environments
conda update package-name              # Update a package
```

> 💡 Use `conda` when working with scientific packages like NumPy, SciPy, TensorFlow, etc.
