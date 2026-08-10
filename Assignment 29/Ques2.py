def main():
    file_name = input("Enter the file name or path: ")

    fobj = open(file_name,"r")
    print("file get open")
    print("file Content...")
    print(fobj.read())
    

if __name__ == "__main__":
    main()