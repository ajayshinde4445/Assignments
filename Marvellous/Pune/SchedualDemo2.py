import schedule
import time
import datetime


def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    # print("Current time is :",datetime.datetime.now()

    print("Automation Script Started :")

    schedule.every(1).minute.do(Display)

    # Issue 



if __name__ == "__main__":
    main()