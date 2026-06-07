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
        
        has_files = False
        
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)
            
            if os.path.isfile(full_path):
                print(f"{full_path} is a file")
                has_files = True
                break
            
        if not has_files:
            print("No files found in this folder.")
            print("1. Delete the empty folder")
            print("2. Add subfolders")
            print("3. Choose another folder")
            try:  
                user_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Error! Please enter a number")
                continue
            
            if user_choice == 1:
                os.rmdir(folder_path)
                print(f"{folder_path} has been successfully deleted.")
                continue
            elif user_choice == 2:
                folder_names = input("Enter folder name (separated by spaces): ")
                
                name_list = folder_names.split()
                
                for name in name_list:
                    folder_full_path = os.path.join(folder_path, name)
                    os.makedirs(folder_full_path, exist_ok = True)
                 
                print(f"Created folders: {', '.join(name_list)}")
                
                continue
                
            elif user_choice == 3:
                continue
            else:
                print("Invalid choice.")

        while(True):
            print("1. Auto sort Feature: ")
            print("2. Manual sort Feature: ")
            print("3. Exit Program: ")
            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Error! Please enter a number.")
                continue
                
            if choice == 1:
                print("Auto-sort feature running...")
                
                files_moved = 0
                folders_created = set()
                
                asked_categories = set()
                
                category_decision = {}
                
                items = os.listdir(folder_path)
                
                for filename in items:
                    filepath = os.path.join(folder_path, filename)
                    
                    if os.path.isfile(filepath):
                        print(f"Found File: {filename}")
                        
                        root, ext = os.path.splitext(filename)
                        
                        category = extension_map.get(ext, "Misc")
                        destination_folder = os.path.join(folder_path, category)
                        conflict_exists = os.path.exists(destination_folder) and os.listdir(destination_folder)
                        os.makedirs(destination_folder, exist_ok = True)
                        folders_created.add(category)
                        destination_path = os.path.join(destination_folder, filename)
                        
                        if conflict_exists and category not in asked_categories:
                            
                            user_input = input(f"Folder '{category}' already has files. Reorganise (move files in) or skip? (r/s): ").lower()
                            category_decision[category] = user_input
                            asked_categories.add(category)
                        else:
                            user_input = category_decision.get(category, "r")
                            
                        if user_input == "s":
                            print(f"Skipping: {filename}")
                            continue
                    
                        shutil.move(filepath, destination_path)
                        print(f"Moved: {filename} -> {category}/")
                        
                        files_moved = files_moved + 1
                        
                print(f"\nSummary:")
                print(f"Folder: {folder_path}")
                print(f"Files moved: {files_moved}")
                break
            elif choice == 2:
                print("Manual sort feature is running...")
                
                folders_created = set()
                
                files_moved = 0
                
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
                    
                    destination_path = os.path.join(destination_folder, selected_filename)
                    
                    source_path = os.path.join(folder_path, selected_filename)
                    
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                        folders_created.add(category)
                        
                    shutil.move(source_path, destination_path)
                    
                    print(f"Moved: {selected_filename} -> {category}/")
                    
                    files_moved = files_moved + 1
                    
                    sort_another_file = input("Sort another file (y/n): ").lower()
                    
                    if sort_another_file == "n" or sort_another_file == "no":
                        break
                    
                print(f"\nSummary:")
                print(f"Folder: {folder_path}")
                print(f"Files moved: {files_moved}")
                print(f"Folders created: {', '.join(folders_created)}")
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