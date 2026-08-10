#  seek(kuthe,kuthun)


def main():
    try:
        fobj = open("Demo.txt","r")
        print("file get opened")

        
        fobj.seek(10,0)

        data  = fobj.read()

        print(data)
    except FileNotFoundError as fobj:
        print("File is not present in current directory")
if __name__ == "__main__":
    main()