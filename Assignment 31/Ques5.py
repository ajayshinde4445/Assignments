print("-"*70)
print("task should write into file current date and time")
print("-"*70)
import datetime
import schedule
import time
def Save():

    fobj = open("demo.txt","a")
    print("check file gets open")

    curent_time = datetime.datetime.now()
    fobj.write(f"Task executed at :{curent_time}\n")
    # fobj.write("Task executed at :",datetime.datetime.now())

def main():
    print("Automation Script Started")
    schedule.every(10).seconds.do(Save)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("Automation Script End")
    

if __name__ == "__main__":
    main()

