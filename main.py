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

