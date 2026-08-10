print("-"*70)
print("save file backup")
print("-"*70)
import datetime
import schedule
import time
import sys
import shutil


def Directoryback():
    border = "-"*40

    TimeStamp =time.ctime()
    LogFileName = "Marvellous%s.log"%(TimeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    print("LogFile backup gets Created with Name :",LogFileName)

    # fobj = open(LogFileName,"w")
    # fobj.write(border+"\n")
    fobj = shutil.copy("demo.txt",LogFileName)

    fobj.write("Marvellous Automation Script \n")
    fobj.write(border+"\n")




    

def main():
    print("Automation script Started...")

    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this automation script is use to backup file")
            print("For better usage please check --u")
        elif(sys.argv[1 == "--u"] or sys.argv[1] == "--U"):
            print("please execute script as")
            print("python file.py directoru name")
            print("directorry name should be absoulte path")
        else:
            schedule.every(1).minute.do(Directoryback.sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Number of argument")
        print("Use --h or --u for more information")
if __name__ == "__main__":
    main()