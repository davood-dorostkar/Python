# 📂 Working With Files in Python

## 1. CSV Files (`csv` module)

CSV (Comma-Separated Values) is a simple format for storing tabular data.


### **Reading CSV Files**

```python
import csv

# Open a file (UTF-8 encoding helps avoid character errors)
my_file = open("file.csv", encoding="utf-8")

# Method 1: Read as lists
data = csv.reader(my_file)
lines = list(data)  # Convert to list
print(lines)

# Method 2: Read as dictionaries (header row becomes keys)
file = open("file.csv", encoding="utf-8")
data = csv.DictReader(file)
for row in data:
    print(row["Name"], row["Age"])  # Access by column name
```

💡 **Tip:** `DictReader` is useful when you want column access by name instead of index.


### **Writing CSV Files**

```python
import csv

output = open("file.csv", mode="w", newline='')  # newline='' avoids blank lines
csv_writer = csv.writer(output, delimiter=',')
csv_writer.writerow(["Name", "Age", "City"])  # Write one row
csv_writer.writerows([["Alice", 25, "Paris"], ["Bob", 30, "London"]])  # Multiple rows

output.close()
```

💡 Always close the file after writing.


### **Full Example: Calculate Totals and Save**

```python
import csv

# Read from CSV
file = open('shop.csv', encoding="utf-8")
data = csv.DictReader(file)

# Prepare results
result = [['Product Name', 'Price', 'Quantity', 'Sum']]
for row in data:
    item_sum = [
        row['Product Name'],
        row['Price'],
        row['Quantity'],
        int(row['Price']) * int(row['Quantity'])  # Calculate total
    ]
    result.append(item_sum)

file.close()

# Write to CSV
output = open('sums.csv', mode='w', newline='')
writer = csv.writer(output, delimiter=',')
for row in result:
    writer.writerow(row)

output.close()
```


## 2. PDF Files (`PyPDF2` module)

`PyPDF2` is a popular library for reading and writing PDFs.


### **Reading a PDF**

```python
import PyPDF2

pdf = PyPDF2.PdfReader("file.pdf")
print(len(pdf.pages))  # Number of pages

first_page = pdf.pages[0]  # Get first page (index starts at 0)
text = first_page.extract_text()  # Extract text
print(text)
```

💡 Page numbers in `PdfReader` are **zero-indexed**.


### **Writing / Merging PDFs**

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.write("merged.pdf")
merger.close()
```

💡 `PdfWriter` lets you create PDFs from scratch or modify pages.


## 3. Excel Files (`openpyxl` module)

`openpyxl` is the go-to library for working with Excel `.xlsx` files.


### **Reading an Excel File**

```python
import openpyxl

wb = openpyxl.load_workbook("file.xlsx")  # Correct function is load_workbook
ws = wb.active  # Get active sheet

# Accessing a cell
cell = ws['C8']
print(cell.value)  # Cell content
print(cell.fill)   # Background fill
```


### **Summing a Range of Cells**

```python
total = 0
for i in range(1, 11):  # Rows 1 to 10 in column A
    cell = ws[f'A{i}']
    total += cell.value

print(total)
```


### **Creating an Excel File**

```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# Write into specific cell
ws['A2'] = 'Davood'

# Append a row
ws.append([1, 2, 3])

# Save the file
wb.save('file.xlsx')
```

💡 `append()` always writes a new row at the end of the sheet.
