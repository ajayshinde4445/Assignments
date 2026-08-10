import schedule
import time
import datetime
import sys
import os
border = "-"*70

def DirectoryScanner(DirectoryPath):

    subcnt = 0
    fcnt = 0
    for FolderName , SubFloder, FileName in os.walk(DirectoryPath):

        for subf in SubFloder:
            
            subcnt = subcnt+1
        for fname in FileName:

            fcnt =fcnt + 1

    print("Directory Scan :E:/",DirectoryPath)
    print("Total Number of Subfolder :",subcnt)
    print("Total Number Of Files :",fcnt)
    print("Scan Time :",datetime.datetime.now())





def main():
    print(border)
    print("Automation Script Sarted")
    print(border)

    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is use to Scan Directory")
            print("For Better understand use -- u flag")
        elif(sys.argv[1] == "-u" or sys.argv[1] =="--U"):
            print("Please execute Script as")
            print("python FileName.py Directoryname")
            print("Directory name should be absoulte path")
        else:

            # DirectoryScanner(sys.argv[1])
            schedule.every(1).minutes.do(DirectoryScanner,sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Number of Argument")
        print("Please use --h or -- u for more information")

    print(border)
    print(" Thank You for using Marvellous Automation Script")
    print(border)



if __name__ == "__main__":
    main()