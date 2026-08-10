import schedule
import time
import datetime


def Display():
    print("Current Date and Time...",datetime.datetime.now())

def main():
    # print("Current time is :",datetime.datetime.now()

    print("Automation Script Started :")

    schedule.every(10).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("ENd Of automation Script")



if __name__ == "__main__":
    main()