import os
import shutil

extension_map = {
                    # For the images
                    ".jpg": "Images",
                    ".jpeg": "Images",
                    ".png": "Images",
                    ".gif": "Images",
                    
                    # For the Documents
                    ".pdf": "Documents",
                    ".txt": "Documents",
                    ".docx": "Documents",
                    
                    # For Music
                    ".mp3": "Music",
                    ".wav": "Music",
                    
                    # For videos
                    ".mp4": "Videos",
                    ".avi": "Videos",
                }

def main():
    
    print("Welcome to your personal File Organizer.")
    
    while(True):
        
        while(True):
            
                
            folder_path = input("Enter folder path: ")
            
            if os.path.exists(folder_path):
                break
            else:
                print("Error. Folder path does not exist. Try again.")
                
        print("Folder path found!")
        
        while(True):
            print("1. Auto sort Feature: ")
            print("2. Manual sort Feature: ")
            print("3. Exit Program: ")
            
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                print("Auto-sort feature running...")
                
                items = os.listdir(folder_path)
                
                for filename in items:
                    filepath = os.path.join(folder_path, filename)
                    
                    if os.path.isfile(filepath):
                        print(f"Found File: {filename}")
                        
                        root, ext = os.path.splitext(filename)
                        
                        category = extension_map.get(ext, "Misc")
                        destination_folder = os.path.join(folder_path, category)
                        os.makedirs(destination_folder, exist_ok = True)
                        
                        destination_path = os.path.join(destination_folder, filename)
                        
                        shutil.move(filepath, destination_path)
                        print(f"Moved: {filename} -> {category}/")
                break
            elif choice == 2:
                print("Manual sort feature is running...")
                
                while True:
                    
                    items = os.listdir(folder_path)
                    files = []
                    for filename in items:
                        filepath = os.path.join(folder_path, filename)
                        
                        if os.path.isfile(filepath):
                            files.append(filename)
                            
                    for index, name in enumerate(files):
                        index += 1
                        print(f"{index}. {name}")
                    
                    while (True):
                        try:
                            file_number = int(input("Choose a file by number: "))
                            if 1 <= file_number <= len(files):
                                break
                            else:
                                print("Number chosen is out of range.")
                        except ValueError:
                            print("Error! You can only insert a number.")
                            
                            
                    selected_index = file_number - 1
                        
                    selected_filename = files[selected_index]
                    
                    print(f"Selected: {selected_filename}")
                    
                    category = input("Enter category folder name: ")
                    
                    destination_folder = os.path.join(folder_path, category)
                    
                    os.makedirs(destination_folder, exist_ok = True)
                    
                    destination_path = os.path.join(destination_folder, selected_filename)
                    
                    source_path = os.path.join(folder_path, selected_filename)
                    
                    shutil.move(source_path, destination_path)
                    
                    print(f"Moved: {selected_filename} -> {category}/")
                    
                    sort_another_file = input("Sort another file (y/n): ").lower()
                    
                    if sort_another_file == "n" or sort_another_file == "no":
                        break
                        
            elif choice == 3:
                print("Exiting program. Goodbye!")
                # Exit the Program
                return
            else:
                print("Invalid choice. Try again")
            
        continue_choice = input("Do you want to organize another folder? (y/n): ")
        if continue_choice == "n":
            break
        
    
if __name__ == "__main__":
    main()