## 🧩 Step 1: Create a simple directory

```bash
mkdir sample
cd sample
```

---

## 🧠 Step 2: Create a virtual environment manually

You can create and name it yourself (like `myenv` instead of `.venv`):

```bash
uv venv myenv
```

This creates an isolated environment under `myenv/`.

---

## 🧮 Step 3: Check Python inside that env

You can directly run a command inside the env without activating it:

```bash
uv run --python myenv/bin/python -- python --version
```

But if you prefer activation:

```bash
source myenv/bin/activate
# On Windows: myenv\Scripts\activate
```

---

## 🧱 Step 4: Add (install) a library without requirements.txt

Let’s install a library (say `requests`):

```bash
uv pip install requests


if file :

uv pip install -r requirements.txt

or 

uv pip sync requirements.txt
```

This installs it **inside your env** — similar to `pip install`, just much faster.

You can confirm it:

```bash
uv pip list
```

---

## 🐍 Step 5: Create a Python script

```bash
echo 'import requests
r = requests.get("https://api.github.com")
print("Status:", r.status_code)
print("Headers:", list(r.headers.keys())[:5])
' > app.py
```

Or manually create `app.py` and paste that code.

---

## 🚀 Step 6: Run the script

### Option 1 (traditional way)

If the env is **activated**, just do:

```bash
python app.py
```

### Option 2 (no activate needed)

Run directly through uv:

```bash
uv run --python myenv/bin/python -- python app.py
```

✅ You’ll see:

```
Status: 200
Headers: ['Server', 'Date', 'Content-Type', 'Content-Length', 'Connection']
```

---

## 🧹 Step 7: Cleanup (optional)

When done:

```bash
deactivate  # if activated
rm -rf myenv
```

---

### 🧠 Recap of what you just did

| Step | Command                         | Description                   |
| ---- | ------------------------------- | ----------------------------- |
| 1    | `uv venv myenv`                 | Created a manual env          |
| 2    | `uv pip install requests`       | Installed a lib without files |
| 3    | `python app.py` or `uv run ...` | Executed code within that env |

This mirrors what you’d do with `python -m venv` + `pip install`, but faster and simpler with `uv`.

---


## Cli OP :


```
❯❯ project-0 git:(main) 21:58 uv venv myenv
Using CPython 3.11.9
Creating virtual environment at: myenv
Activate with: myenv\Scripts\activate
❯❯ project-0 git:(main) 21:58 uv venv myenv
Using CPython 3.11.9
Creating virtual environment at: myenv
Activate with: myenv\Scripts\activate
❯❯ project-0 git:(main) 22:00 myenv\Scripts\activate
 (myenv) ❯❯ project-0 git:(main) 22:00 uv pip install requests
Creating virtual environment at: myenv
Activate with: myenv\Scripts\activate
❯❯ project-0 git:(main) 22:00 myenv\Scripts\activate
 (myenv) ❯❯ project-0 git:(main) 22:00 uv pip install requests
Using Python 3.11.9 environment at: myenv
❯❯ project-0 git:(main) 22:00 myenv\Scripts\activate
 (myenv) ❯❯ project-0 git:(main) 22:00 uv pip install requests
Using Python 3.11.9 environment at: myenv
Resolved 5 packages in 149ms
Installed 5 packages in 71ms
 (myenv) ❯❯ project-0 git:(main) 22:00 uv pip install requests
Using Python 3.11.9 environment at: myenv
Resolved 5 packages in 149ms
Installed 5 packages in 71ms
Using Python 3.11.9 environment at: myenv
Resolved 5 packages in 149ms
Installed 5 packages in 71ms
 + certifi==2025.8.3
Resolved 5 packages in 149ms
Installed 5 packages in 71ms
 + certifi==2025.8.3
 + charset-normalizer==3.4.3
 + certifi==2025.8.3
 + charset-normalizer==3.4.3
 + idna==3.10
 + requests==2.32.5
 + urllib3==2.5.0
 + charset-normalizer==3.4.3
 + idna==3.10
 + requests==2.32.5
 + urllib3==2.5.0
 + idna==3.10
 + requests==2.32.5
 + urllib3==2.5.0
 (myenv) ❯❯ project-0 git:(main) 22:01 python app.py
 (myenv) ❯❯ project-0 git:(main) 22:01 python app.py
Status: 200
Headers: ['Date', 'Content-Type', 'Cache-Control', 'Vary', 'ETag']
 (myenv) ❯❯ project-0 git:(main) 22:01 deactivate
❯❯ project-0 git:(main) 22:01

```