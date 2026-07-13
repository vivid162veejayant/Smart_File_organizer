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
    "Others": []  # For files that don't match any of the above categories
}

folder = Path(r"D:\Veejayant Personal\Coding\Projects\Python Projects\Smart File Organizer\Testing\Downloads")

for file in folder.iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()  # Get the file extension in lowercase
        moved = False  # Flag to check if the file has been moved

        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_folder = folder / category
                destination_folder.mkdir(exist_ok=True)  # Create the category folder if it doesn't exist
                shutil.move(str(file), str(destination_folder / file.name))  # Move the file to the category folder
                print(f"Moved {file.name} to {category} folder.")
                moved = True
                break

        if not moved:
            others_folder = folder / "Others"
            others_folder.mkdir(exist_ok=True)  # Create the Others folder if it doesn't exist
            shutil.move(str(file), str(others_folder / file.name))  # Move the file to the Others folder
            print(f"Moved {file.name} to Others folder.")
            