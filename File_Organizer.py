import os

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
            print("3. Exiting Program: ")
            
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                print("Auto-sort feature running...")
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