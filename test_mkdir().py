from pathlib import Path

folder = Path(r"D:\Veejayant Personal\Coding\Projects\Python Projects\Smart File Organizer\Testing\Downloads\Images")

folder.mkdir(exist_ok=True)  # Create the folder if it doesn't exist, and do nothing if it does exist

print("Folder created!")
