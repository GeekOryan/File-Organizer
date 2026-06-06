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
                print("Manual sort feature running...")
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