import pathlib as path

folder= path.Path("Downloads")
for item in folder.iterdir():
    if item.is_file():
        print(item.name, "-->", item.suffix)


categories = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".exe": "Applications",
}


files = {
    "cat":"animal",
    "car":"vehicle",
    "apple":"food",
}

print(files["cat"])

extension = ".png"

print(categories[extension])
