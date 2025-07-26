# Python Basics & Usage Guide

This repository serves as a beginner-friendly reference to understand the fundamentals of Python—its origins, purpose, how to run Python code from different environments, and a few extra pointers for getting started effectively.

---

## What is Python?

Python is a high-level, interpreted programming language known for its readability and simplicity. Its syntax is clean and close to natural language, making it a great choice for beginners, while still being powerful enough for large-scale systems and production-level code.

---

## Why Was Python Created?

Python was designed to make programming intuitive and efficient. Its goals were:

- Simplicity and minimalism in syntax
- Easy readability and maintainability
- Support for both scripting and large application development

It emphasizes reducing the cost of program maintenance and encourages code reuse and modularity.

---

## When and Who Created Python?

- Created by: **Guido van Rossum**
- First released: **1991**
- Developed at: **Centrum Wiskunde & Informatica (CWI), Netherlands**

Python was influenced by languages like ABC and Modula-3, and was intended as a general-purpose language that promotes productivity.

---

## How to Run Python Code

Python supports multiple ways of executing code, depending on the file type or environment.

### 1. Running a `.py` File

Write your code in a file with `.py` extension:

```python
# hello.py
print("Hello, Python")
````

Then execute it in a terminal or command prompt:

```bash
python hello.py
```

If `python` points to Python 2.x, use:

```bash
python3 hello.py
```

---

### 2. Running a `.ipynb` File (Jupyter Notebook)

Notebooks are often used for experimentation, data analysis, and teaching.

To run a notebook:

1. Install Jupyter:

```bash
pip install notebook
```

2. Start Jupyter server:

```bash
jupyter notebook
```

3. It will open in the browser. Select and open your `.ipynb` file, then run each cell using `Shift + Enter`.

---

### 3. Running Code from the Command Line (CLI)

You can run small code snippets directly:

```bash
python -c "print('Hello from CLI')"
```

Or open the interactive Python shell:

```bash
python
```

Then type Python commands line by line.

---

### 4. Running Code from an IDE or Code Editor

Popular IDEs and editors:

* Visual Studio Code (with Python extension)
* PyCharm (Community or Professional)
* JupyterLab
* Sublime Text

Most of these editors support running code inline, setting breakpoints, debugging, and managing virtual environments.

---

## Setting Up Python Locally

1. Download and install Python from the official website:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Check installation:

```bash
python --version
# or
python3 --version
```

3. Install packages using pip:

```bash
pip install package-name
```

---

## Using Virtual Environments

To avoid package conflicts, it's recommended to use virtual environments for each project.

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

* On macOS/Linux:

```bash
source venv/bin/activate
```

* On Windows:

```bash
venv\Scripts\activate
```

Deactivate when done:

```bash
deactivate
```

---

## Making Python Files Executable

For Unix-like systems:

1. Add the shebang line at the top of your file:

```python
#!/usr/bin/env python3
```

2. Make the file executable:

```bash
chmod +x script.py
```

3. Run it directly:

```bash
./script.py
```

---

## Recommended Project Structure

```bash
project/
├── main.py
├── module/
│   ├── __init__.py
│   └── helper.py
├── requirements.txt
└── README.md
```

Install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## When to Use Python

Python is widely used in:

* Web development (Flask, Django, FastAPI)
* Data science and machine learning (NumPy, Pandas, Scikit-learn, TensorFlow)
* Automation and scripting
* DevOps and infrastructure tooling
* Backend API development
* Education and training

---

## References

* Official documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
* PEP 8 coding style: [https://pep8.org/](https://pep8.org/)
* Python Package Index (PyPI): [https://pypi.org/](https://pypi.org/)
