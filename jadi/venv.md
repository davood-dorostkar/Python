# Virtual Environment (venv)

Installing packages system-wide can cause conflicts.
A **virtual environment** keeps dependencies isolated.

```sh
python -m venv my_env   # create venv (often named "venv")
```

Activate it:

```sh
source my_env/bin/activate   # Linux/Mac
my_env\Scripts\activate      # Windows
```

Install packages without interfering with global Python:

```sh
pip install flask
```

Deactivate:

```sh
deactivate
```

Export & recreate environments:

```sh
pip list      # human-readable
pip freeze    # machine-readable

pip freeze > requirements.txt
pip install -r requirements.txt
```
