# 🌐 Working with Web Modules in Python

## 1. API Basics

**API** stands for **Application Programming Interface**.
It’s a set of rules that allows two applications to talk to each other.

* **Why it’s important:** Lets different systems share and use data.
* **Why we use it:** Instead of downloading a file manually, APIs give structured data (often JSON) directly to our code.


## 2. REST & JSON

**REST** is an architecture style for APIs that uses HTTP requests like:

* `GET` → retrieve data
* `POST` → send data
* `PUT` → update data
* `DELETE` → remove data

Most modern APIs use **JSON** (JavaScript Object Notation) to send and receive data.


### JSON in Python

```python
import json

# Python dictionary
data = {'name': 'davood', 'age': 34, 'hobby': 'hiking'}

# Convert Python object → JSON string
json_data = json.dumps(data)
print(json_data)
# '{"name": "davood", "age": 34, "hobby": "hiking"}'

# Convert JSON string → Python object
received_data = json.loads(json_data)
print(received_data)
# {'name': 'davood', 'age': 34, 'hobby': 'hiking'}
```

💡 `dumps` = Python → JSON
💡 `loads` = JSON → Python


## 3. Getting Data from an API

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()  # Directly parse JSON response
print(data)
```

💡 `requests` automatically detects and parses JSON if you call `.json()`.


### Example: Open Notify API (Astronauts in Space)

```python
import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
data = response.json()

print(f"There are {data['number']} people in space right now:")
for person in data['people']:
    print(f"- {person['name']} on {person['craft']}")
```

Example output:

```
There are 12 people in space right now:
- Oleg Kononenko on ISS
- Nikolai Chub on ISS
...
```


## 4. Sending Data to an API (POST request)

```python
import requests

data = {"name": "Ali", "age": 25}
response = requests.post("https://api.example.com/users", json=data)

print(response.status_code)  # e.g., 201 for "Created"
```

💡 You don’t need `json.dumps()` — `requests` handles it if you pass `json=data`.


### Adding Headers to a Request

Custom headers are often needed for authentication or special API settings.

```python
import requests

headers = {
    'Custom-Header': 'Value',
    'Authorization': 'Bearer YOUR_TOKEN'
}

response = requests.get('https://api.example.com/data', headers=headers)
print(response.json())
```

Other request parameters:

* **`auth=('user', 'pass')`** → Basic authentication
* **`params={'page': 2}`** → Add query parameters to a GET request
* **`timeout=5`** → Prevent hanging requests


## 5. Building Your Own API with Flask

If you want to be **the one providing an API**, you need a web server framework like:

* Flask
* FastAPI
* Django


### Minimal Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```


### Running the Flask Server

```sh
flask --app hello run  # "hello.py" is the Python file name 
```

This will start a local server at `http://127.0.0.1:5000/`.
