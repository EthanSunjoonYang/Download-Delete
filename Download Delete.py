import os

#Path to the downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Classify the types of documents that are typically the "junk" in my downloads folder
download_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.dmg',)

#Loop through all files in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    #Files that meet the junk criteria are deleted
    if os.path.isfile(file_path) and file_path.lower().endswith(download_extensions):
        try:
            os.unlink(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

print("All downloaded junk has been deleted!")