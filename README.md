# File Organizer

## About
A Python command-line tool that automatically or manually organises files 
in any folder into categorised subfolders. Built for developers, IT and 
Computer Science students, and anyone who works with cluttered directories 
and wants a faster, more efficient way to sort their files without touching 
the file manager.

## Features
: **Auto Sort** — automatically detects every file's extension and moves 
  it into the correct category subfolder (Images, Documents, Music, 
  Videos, Misc)
: **Manual Sort** — displays all files by number, lets you select each 
  file individually and name your own destination subfolder
: **Conflict Detection** — if a category subfolder already exists with 
  files in it, prompts you to reorganise or skip before moving anything
: **Empty Folder Handling** — if the selected folder has no files, offers 
  options to delete the folder, create new subfolders, or choose a 
  different path
: **Summary Report** — after every sort operation displays the folder 
  path, number of files moved and all subfolders created
: **Organise Multiple Folders** — after finishing, prompts to organise 
  another folder or exit cleanly

## Supported File Types

| Category  | Extensions                        |
|-----------|-----------------------------------|
| Images    | .jpg, .jpeg, .png, .gif           |
| Documents | .pdf, .txt, .docx                 |
| Music     | .mp3, .wav                        |
| Videos    | .mp4, .avi                        |
| Misc      | anything not in the above list    |

## How to Run

**Requirements:** Python 3 installed on your machine.

**Clone the repository:**
```bash
git clone https://github.com/GeekOryan/file-organizer.git
```

**Navigate into the folder:**
```bash
cd file-organizer
```

**Run the program:**
```bash
python organizer.py
```

**When prompted, enter a full folder path, for example:**

## Author: Oryan
