import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} Created successfully.")
    except FileExistsError:
        print(f"File Name {filename} already exists.")
    except Exception as E:
        print(f"Error Occured: {E}")

    
def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files in directory.")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename} has been deleted successfully.")
    except FileNotFoundError:
        print(f"File not found")
    except Exception as e:
        print(f"Error Occured: {e}")


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f'Content of {filename} :\n{content}')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print(f"Error Occured: {e}")


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            print(f"{filename} doesn't exist!")
            content = input("Enter new data to add : ")
            f.write(content + "\n")
            print(f'Content added to {filename} successfully.')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as F:
        print(f"Error Occured: {F}")



def main():
    while True:
        print("---> File Management System <---")
        print("1. Create a file.")
        print("2. View all files in directory.")
        print("3. Delete a file.")
        print("4. Read a file.")
        print("5. Edit a file.")
        print("6. Exit")

        choice = input("enter your choice(1-6): ")

        if choice == '1':
            filename = input("Enter file name to create: ")
            create_file(filename)
        
        elif choice == '2':
            view_all_files()
        
        elif choice == '3':
            filename = input("Enter file name to delete: ")
            delete_file(filename)
        
        elif choice  == '4':
            filename = input("Enter file name to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter file name to edit: ")
            edit_file(filename)
        
        elif choice ==  '6':
            print("Thank you for using File Management System.")
            print("Closing the system ...")
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()