import os

folder_path = "test_folder"
files = os.listdir(folder_path)

cat={
    ".png": "images",
    ".mp4": "videos",
    ".jpg": "images",
    ".pdf": "pdfs"
}

for file in files:
    name, extension = os.path.splitext(file)
    if extension in cat:
        folder_name = cat[extension]
        os.makedirs(folder_name, exist_ok=True)
        old_path = os.path.join(folder_path,file)
        new_path = os.path.join(folder_name,file)
        os.rename(old_path,new_path)
    else:
        print(f"{file} don't know it")