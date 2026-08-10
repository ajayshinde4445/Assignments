def main():
    try:
        fobj = open("Demo.txt","r")
        print("file get opened")

        print("file offset is :",fobj.tell())

        data = fobj.read(10)

        print(data)

        print("file offset is :",fobj.tell())

        data = fobj.read(10)

        print(data)

        print("file offset is :",fobj.tell())

        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")
if __name__ == "__main__":
    main()