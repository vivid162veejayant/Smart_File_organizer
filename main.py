from pathlib import Path
import shutil
import hashlib

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

folder = Path()



total_moved = 0

category_count = {category: 0 for category in categories}

hash_memory = set()


def get_hash(file_path):
    with open(file_path, "rb") as file:
        data = file.read()

    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.hexdigest()


for file in folder.rglob("*"):

    # Skip anything that isn't a file
    if not file.is_file():
        continue

    # Skip files already inside organizer folders
    if file.parent.name in categories:
        continue

    try:
        file_hash = get_hash(file)
    except (PermissionError, OSError) as e:
        print(f"Skipped: {file}")
        print(f"Reason : {e}")
        continue


    if file_hash in hash_memory:
        print(f"Duplicate Detected! {file}")
        continue

    hash_memory.add(file_hash)

    file_extension = file.suffix.lower()
    moved = False

    for category, extensions in categories.items():

        if file_extension in extensions:

            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file.name

            counter = 1
            while destination.exists():
                new_name = f"{file.stem}_{counter}{file.suffix}"
                destination = destination_folder / new_name
                counter += 1

            try:
                print(f"Moving from: {file}")
                print(f"Moving to:   {destination}")

                shutil.move(str(file), str(destination))

                total_moved += 1
                category_count[category] += 1

            except (PermissionError, OSError) as e:
                print(f"Skipped: {file}")
                print(f"Reason : {e}")

            moved = True
            break

    if not moved:

        others_folder = folder / "Others"
        others_folder.mkdir(exist_ok=True)

        destination = others_folder / file.name

        counter = 1
        while destination.exists():
            new_name = f"{file.stem}_{counter}{file.suffix}"
            destination = others_folder / new_name
            counter += 1

        try:
            print(f"Moving from: {file}")
            print(f"Moving to:   {destination}")

            shutil.move(str(file), str(destination))

            total_moved += 1
            category_count["Others"] += 1

        except (PermissionError, OSError) as e:
            print(f"Skipped: {file}")
            print(f"Reason : {e}")

print("\n============== Summary ==============")

for category, count in category_count.items():
    print(f"{category}: {count} files moved")

print(f"\nTotal files moved: {total_moved}")