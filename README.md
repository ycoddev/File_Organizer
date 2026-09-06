# File Organizer 🗂️

A simple Python script that automatically organizes files in a folder by type — moving images, PDFs, and videos into their own subfolders.

## Features
- Automatically detects file type by extension
- Creates category folders if they don't exist
- Moves each file into its matching folder
- Warns about unrecognized file types instead of breaking

## Tech Stack
- Python 3
- `os` module (file/folder handling)

## How to Use
1. Place the script in the same directory as the folder you want to organize
2. Update `folder_path` to match your target folder's name
3. Run the script:
```bash
python main.py
```

## Example
**Before:**
test_folder/
photo.jpg
document.pdf
video.mp4


**After:**
images/
photo.jpg
pdfs/
document.pdf
videos/
video.mp4

---
🇪🇬 [النسخة العربية](README.ar.md)
