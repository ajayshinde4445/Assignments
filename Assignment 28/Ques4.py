print("-" * 70)
print("write prog which accept a file name from the user and " \
"counts how many lines are present in the line:")
print("-" * 70)

def main():
    
    try:
        file_name = input("Enter the file name (e.g, sample.txt): ")
        dest_name = input("Enter the file name (e.g, sample.txt): ")

        fobj = open(file_name,"r")

        fobj2 = open(dest_name,"w")
        # count = 0
        print("file get open")

        fobj2.write(fobj.read())

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()
