from pathlib import Path
import shutil

# Dictionaries for extensions and their corresponding folder names
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Scripts": [".py", ".js", ".html", ".css", ".php", ".sh", ".bat"],
    "Executables": [".exe", ".msi", ".apk", ".bin"],
    "Others": []
}

folder = Path("Downloads")

total_moved = 0

category_count = {
    "Images": 0,
    "Videos": 0,
    "Documents": 0,
    "Audio": 0,
    "Archives": 0,
    "Scripts": 0,
    "Executables": 0,
    "Others": 0
}

for file in folder.iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()
        moved = False

        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_folder = folder / category
                destination_folder.mkdir(exist_ok=True)

                source = file
                destination = destination_folder / file.name

                # Duplicate protection with automatic renaming
                if destination.exists():
                    counter = 1

                    while destination.exists():
                        new_name = file.stem + "_" + str(counter) + file.suffix
                        destination = destination_folder / new_name
                        counter += 1

                print("Moving from:", source)
                print("Moving to:", destination)

                shutil.move(str(source), str(destination))

                total_moved += 1
                category_count[category] += 1

                moved = True
                break

        if not moved:
            others_folder = folder / "Others"
            others_folder.mkdir(exist_ok=True)

            destination = others_folder / file.name

            if destination.exists():
                counter = 1

                while destination.exists():
                    new_name = file.stem + "_" + str(counter) + file.suffix
                    destination = others_folder / new_name
                    counter += 1

            shutil.move(str(file), str(destination))

            
            
print("\n==============Summary==============")

for category, count in category_count.items():
    print(f"{category}: {count} files moved")
    print(f"\nTotal files moved: {total_moved}")