# 🖼 Working with Images 

## 📦 Pillow (PIL Fork)

[Pillow Documentation](https://pillow.readthedocs.io/en/stable/index.html)

Pillow is a popular image processing library in Python — it can open, manipulate, and save many image file formats.


## 🛠 Basic Usage

```python
from PIL import Image

# Open an image
img = Image.open("example.jpg")  

# Load image into memory (optional, but good for performance)
img.load()

# Show the image
img.show()

# Image information
print(img.info)       # Metadata
print(img.size)       # (width, height)
print(img.filename)   # File path
print(img.format)     # JPEG, PNG, etc.
print(img.mode)       # RGB, RGBA, L, etc.
```

📍 **Note:** Pillow uses a **Cartesian coordinate system** with `(0,0)` at the **top-left corner**.


## 🔄 Image Manipulation

### Rotate

```python
rotated = img.rotate(45)  # Degrees
rotated.show()
```

### Crop

```python
cropped = img.crop((100, 100, 300, 300))  # (left, top, right, bottom)
cropped.show()
```

### Paste

```python
overlay = Image.open("logo.png")
img.paste(overlay, (50, 50))  # Top-left position
img.show()
```

### Save

```python
img.save("output.png")  # Format auto-detected from extension
```


## 🎨 Pixel Operations

### Get Pixel Value

```python
pixel = img.getpixel((10, 10))
print(pixel)  # (R, G, B) or (R, G, B, A)
```

### Set Pixel Value

```python
img.putpixel((10, 10), (255, 0, 0))  # Red pixel
```

### Add Transparency

```python
img.putalpha(128)  # 0 = fully transparent, 255 = fully opaque
```


## 📏 Resize & Transform

```python
resized = img.resize((200, 200))
resized.show()

# Transform with affine matrix
transformed = img.transform((400, 400), Image.AFFINE, (1, 0.5, 0, 0.5, 1, 0))
transformed.show()
```


## 🧩 Other Useful Tools in Pillow

* **`ImageFilter`** → blur, sharpen, edge detection
* **`ImageEnhance`** → adjust brightness, contrast, color
* **`ImageDraw`** → draw shapes and text on images
* **`ImageFont`** → use custom fonts for text rendering

Example:

```python
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 40)
draw.text((50, 50), "Hello!", fill="white", font=font)
img.show()
```


## 🕵️ Steganography Example — Hide & Retrieve Messages

We can hide text inside an image by modifying pixel values (lossless formats like PNG are required to avoid data corruption).

```python
from PIL import Image
import os

def encrypt(msg, path):
    img = Image.open(path)
    for i in range(0, img.size[0], 10):  # Every 10 pixels (x)
        for j in range(0, img.size[1], 10):  # Every 10 pixels (y)
            if msg:
                r = ord(msg[0])  # Convert character → ASCII code
                g, b = img.getpixel((i, j))[1:]  # Keep G & B
                img.putpixel((i, j), (r, g, b))
                msg = msg[1:]  # Move to next character
    root, _ = os.path.splitext(path)
    img.save(root + '-enc.png', format='PNG')  # Must be PNG!

def decrypt(path):
    img = Image.open(path)
    hidden_text = ''
    for i in range(0, img.size[0], 10):
        for j in range(0, img.size[1], 10):
            r = img.getpixel((i, j))[0]  # Red channel
            hidden_text += chr(r)  # ASCII → character
    print(hidden_text[:100])  # Print first 100 chars

if __name__ == "__main__":
    # Encrypt
    path1 = "davood-cartoon.jpg"
    msg = "The only way to do great work is to love what you do."
    encrypt(msg, path1)

    # Decrypt
    path2 = "davood-cartoon-enc.png"
    decrypt(path2)
```

### Why PNG and Not JPEG?

JPEG is **lossy**, meaning it slightly changes pixel values during compression.
If you hide data in exact pixel values, JPEG will **destroy or corrupt** it.


## ✅ Summary Table of Pillow Methods

| Method        | Purpose                           |
| ------------- | --------------------------------- |
| `open()`      | Load image from file              |
| `load()`      | Force image data into memory      |
| `show()`      | Preview in default viewer         |
| `info`        | Get metadata                      |
| `size`        | Get dimensions (W,H)              |
| `filename`    | Get file path                     |
| `format`      | Get file format                   |
| `mode`        | Get color mode                    |
| `rotate()`    | Rotate by degrees                 |
| `crop()`      | Crop to given box                 |
| `paste()`     | Paste another image               |
| `save()`      | Save to file                      |
| `getpixel()`  | Get pixel color                   |
| `putpixel()`  | Change pixel color                |
| `putalpha()`  | Change transparency               |
| `resize()`    | Resize image                      |
| `transform()` | Apply affine/projective transform |
