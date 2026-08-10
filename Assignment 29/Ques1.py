from pathlib import Path

# 1. Accept file name from the user
file_name = input("Enter the file name or path: ")

# 2. Create a Path object
file_path = Path(file_name)

# 3. Check if it exists and is a file
if file_path.is_file():
    print(f"Success: '{file_name}' exists.")
else:
    print(f"Error: '{file_name}' does not exist.")