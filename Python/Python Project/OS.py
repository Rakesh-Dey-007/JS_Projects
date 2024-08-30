import os

def list_directory_contents(path='/'):
    try:
        # Get the list of all files and directories
        dir_contents = os.listdir(path)
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist")
    except PermissionError:
        print(f"Permission denied to access {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to list the contents of the current directory
list_directory_contents()
