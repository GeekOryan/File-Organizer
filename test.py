import os

# Checks whether a file or directory exists at the specified path.

# Check if a file exists
if os.path.exists("data.txt"):
    print("File Exists")
else:
    print("File not found")
    
# Check if a directory exists
if os.path.exists("/home/user/documents"):
    print("Directory exists")
    
# os.path.splitext()
# The purpose of this is that it splits a file path into a tuple
# containing (root, extension). The extension includes the dot.

import os

filename = "document.pdf"
root, ext = os.path.splitext(filename)
print(f"Root: {root}") # The output will be document
print(f"Extension: {ext}") # The output will be .pdf

# With the full path
path = "/home/user/archive.tar.gz"
root, ext = os.path.splitext(path)
print(f"Root: {root}") # The output: /home/user/archive.tar
print(f"Extension: {ext}") # Output: .gz

# The best use cases for this is: File type checking, renaming files
# Changing extensions.

# os.listdir(): Returns a list of all files and directories in the specified directory.
import os

items = os.listdir(".")
print(items) # ['file1.txt', 'folder1', 'script.py', ...]

# List specific directory
docs = os.listdir("/home/user/Documents")
for item in docs:
    print(item)
    
# Excludes '.' and '..' entries

# os.path.isfile()
# Checks if a path points to a regular file (not a directory or special file).

import os

# Check if item is a file
if os.path.isfile("config.txt"):
    print("config.txt is a regular file")
    
# Combined with listdir
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"{item} is a file")
    else:
        print(f"{item} is a directory")

# os.makedirs()

# Creates directories recursively, creating all intermediate 
# directories if they don't exist.

import os

# Create single directory
os.makedirs("new_folder")

# Create nested directories
os.makedirs("project/data/2024/logs") # Creates all missing directories

# With exist_ok=True
os.makedirs("existing_folder", exist_ok = True) # No error if it already exists

# Setting specific permissions (Unix)
os.makedirs("secure_folder", mode = 0o755)


# PRACTICAL EXAMPLE:

def organize_files(directory):
    """Organize files by extension into subdirectories"""
    
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist")
        return
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            # Get file extension
            name, ext = os.path.splitext(filename)
            ext = ext[1:] if ext else "no_extension" # Removes the dot.
            
            # Create folder for this extension
            target_dir = os.path.join(directory, ext)
            os.makedirs(target_dir, exist_ok = True)
            
            # Move file (using shutil in real code)
            # shutil.move(filepath, os.path.join(target_dir, filename))
            print(f"Would move {filename} to {ext}/")
            
# Usage
organize_files("./downloads")


# Write a script that asks the user for a folder path, checks if it exists
# and prints whether it was found or not.


folder_path = input("Enter the folder path you want to check: ")

if os.path.exists(folder_path):
    print("The folder path exists")
else:
    print("The folder path does not exist.")

# Test 2: Write a script that lists every file in your current folder and 
# prints only the files, not the subfolders.

items = os.listdir(".")
print(items)

for item in items:
    if os.path.isfile(item):
        print(item)

# Test 3: Write a script that takes a filename like photo.jpg
# and prints the extension separately without the dot.

photo_file = "photo.jpg"

result = os.path.splitext(photo_file)

ext_with_dot = result[1]

ext_without_dot = ext_with_dot[1:]

print(ext_without_dot)
# Test 4: Write a script that creates a subfolder called TestFolder
# inside your current directory. Use exist_ok=True so it doesn't crash
# if the folder already exists.


os.makedirs("TestFolder", exist_ok = True)