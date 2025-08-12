# 🕸 Web Scraping in Python

**Goal:** Automate retrieving, parsing, and extracting data from websites.

## 📦 Required Packages

```bash
pip install requests bs4 lxml selenium 

# for debian based:
sudo apt install python3-requests python3-bs4 python3-lxml python3-selenium 
```


## 📡 HTTP Libraries (from low to high level)

| Library    | Level    | Use Case                             |
| ---------- | -------- | ------------------------------------ |
| `socket`   | Very Low | Direct TCP/HTTP communication        |
| `urllib`   | Medium   | Built-in HTTP requests, URL handling |
| `requests` | High     | Easiest, most common for scraping    |


## 🌐 `requests` — Simple HTTP Requests

```python
import requests

# Basic GET request
r = requests.get("https://example.com")
data = r.text  # The page content (HTML)
print(data[:200])  # First 200 chars
```

### Other Useful Methods

```python
# Send POST request
payload = {"username": "user", "password": "pass"}
r = requests.post("https://httpbin.org/post", data=payload)

# Custom headers
headers = {"User-Agent": "MyScraper 1.0"}
r = requests.get("https://example.com", headers=headers)

# JSON response
r_json = requests.get("https://api.github.com").json()

# Check status
print(r.status_code)  # 200 means OK
```


## 🍲 `BeautifulSoup` — HTML/XML Parsing

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(data, "html.parser")  # or "lxml" for speed
```

### Extracting Data

```python
title_tag = soup.select('title')[0]  # select returns a list
print(title_tag.get_text())  # Page title

# Get all divs
divs = soup.find_all('div')

# Shortcut if you know the element
header1 = soup.h1.text
```


### CSS Selector Examples

```python
soup.select('.my_class')    # Class
soup.select('#my_id')       # ID
soup.select('p > div')      # Direct child
soup.select('ul li a')      # Nested selection
```


### `find_all` vs `select`

| Method       | Syntax Style    | Example                            |
| ------------ | --------------- | ---------------------------------- |
| `find_all()` | HTML attributes | `soup.find_all('div', class_='x')` |
| `select()`   | CSS selectors   | `soup.select('div.x')`             |


### Useful Tag Methods

```python
el = soup.find(id="main")
print(el.get("class"))  # Get attribute value

# Summary table
# find_all(class_="x")  -> list of matches
# find_all(id="x")      -> list of matches
# find(id="x")          -> first match
# select("#x")          -> CSS selector match
# tag.get("id")         -> get attribute from tag
```


## 🖥 Browser Developer Tools for Scraping

* **Inspect element** → Right-click → *Inspect*
* **View page source** → Ctrl+U
* **Element picker** → Click pointer icon in dev tools
* **Copy selector** → Right-click → Copy → *CSS Selector*
* Use Chrome/Firefox extensions to get exact selectors (like `css selector plugin`)


## 🤖 `selenium` — Browser Automation

Use Selenium when:

* JavaScript loads data dynamically
* You need to scroll, click, or interact

📄 Docs: [Selenium Python](https://selenium-python.readthedocs.io/)

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # or Chrome()
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()
```


## ✅ Quick Summary

| Tool            | Purpose                      | Example                            |
| --------------- | ---------------------------- | ---------------------------------- |
| `requests`      | Fetch page HTML              | `requests.get(url)`                |
| `BeautifulSoup` | Parse HTML/XML, extract data | `soup.select('.class')`            |
| `selenium`      | Automate browser actions     | `driver.find_element(...).click()` |
