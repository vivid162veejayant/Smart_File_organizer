from pathlib import Path
import shutil

downloads = Path(r"D:\Veejayant Personal\Coding\Projects\Python Projects\Smart File Organizer\Testing\Downloads")

source = downloads / "photo.png"
destination = downloads / "Images" / "photo.png"

print(source)
print(destination)