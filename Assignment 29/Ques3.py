print("-" * 70)
print("write prog which accept a file name from the user and " \
"counts how many lines are present in the line:")
print("-" * 70)
import sys
def main():
    
    try:
        file_name = sys.argv[1]
        dest_name = sys.argv[2]

        fobj1 = open(file_name,"r")

        fobj2 = open(dest_name,"w")
        # count = 0
        print("file get open")

        fobj2.write(fobj1.read())

        print("content Copy")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()
