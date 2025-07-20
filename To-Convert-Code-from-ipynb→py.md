* **Jupyter Notebooks** use `.ipynb` files (which store code as JSON with cells).
* **Normal Python scripts** use `.py` files (plain text).

---

## ✅ To Convert Code from `.ipynb` → `.py`

There are **2 simple ways** to move code from a Jupyter notebook to a `.py` file:

---

### 🔹 **Option 1: Manually Copy Code**

1. Open your notebook.
2. Copy the code from each cell.
3. Paste it into a `.py` file in VS Code or any editor.
4. Run it from terminal:

   ```bash
   python your_script.py
   ```

> 💡 Jupyter code is **just Python**, so it works fine in `.py` if you remove magic commands like `%matplotlib inline`, etc.

---

### 🔹 **Option 2: Export Notebook as Python Script**

1. In the Jupyter Notebook UI:

   * Go to `File` > `Download as` > `Python (.py)`
   * This will download a `.py` file with all your code.

2. You can then open and edit it in VS Code or run from terminal:

   ```bash
   python exported_script.py
   ```

---

### ⚠️ Few Notes:

* Markdown cells are converted into comments in the `.py` file.
* Interactive plots and outputs are not exported — only code.
* Remove `%` or `!` commands (used in Jupyter only) before running in `.py`.

---
