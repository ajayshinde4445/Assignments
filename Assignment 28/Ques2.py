print("-" * 70)
print("write prog which accept a file name from the user and " \
"counts how many lines are present in the line:")
print("-" * 70)

def main():
    
    try:
        file_name = input("Enter the file name (e.g, sample.txt): ")
        fobj = open(file_name,"r")
        count = 0
        print("file get open")

        for line in  fobj:
            count += len(line.split())
        print("-" * 50)
        print("line count :",count)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()
