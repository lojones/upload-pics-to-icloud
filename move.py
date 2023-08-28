import os
import shutil
import re

def sanitize_path(path):
    """Converts path to a sanitized string with special characters and spaces replaced with '-'."""
    # Replace path separators with '-'
    sanitized = path.replace(os.sep, '-')
    # Replace any sequence of non-alphanumeric characters with a single '-'
    sanitized = re.sub(r'[^a-zA-Z0-9]+', '-', sanitized)
    return sanitized

def move_and_rename_pictures(root_folder):
    # Destination folder
    dest_folder = "e:\\Jane\\all\\iphotolib_modifieds"
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Walk through root folder and its subdirectories
    for foldername, subfolders, filenames in os.walk(root_folder):
        # Skip the destination folder
        if foldername == dest_folder:
            continue

        for filename in filenames:
            # Checking file extension for images (add or remove as needed)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff')):
                # Create the new file name based on the folder path
                rel_folder = os.path.relpath(foldername, root_folder)
                file_root, file_ext = os.path.splitext(filename)
                new_filename = sanitize_path(rel_folder) + '-' + sanitize_path(file_root) + file_ext
                source = os.path.join(foldername, filename)
                destination = os.path.join(dest_folder, new_filename)
                
                # Move and rename the picture
                shutil.move(source, destination)
                print('Moved and renamed "%s" to "%s"' % (source, destination))

if __name__ == "__main__":
    root_folder = 'E:\\Jane\\iPhoto Library\\Modified'  # Current directory
    move_and_rename_pictures(root_folder)
