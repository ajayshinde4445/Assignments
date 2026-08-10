import sys

def main():
    

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is use to Travel Directory")
            print("for better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please excute script as")
            print("python FileName.py directoryname")
            print("Directory name should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name :",DirectoryName)

    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information")
        
if __name__ == "__main__":
    main()