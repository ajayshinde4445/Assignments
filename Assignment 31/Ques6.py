print("-"*70)
print("print lunch time and wrap up time with seperate function")
print("-"*70)
import datetime
import schedule
import time

def Lunch_time():
    print("Lunch Time !")

def Out_time():
    print("Wrap Up Work...")

def main():
    print("Automation script Started...")

    schedule.every().day.at("14:21").do(Lunch_time)
    schedule.every().day.at("14:22").do(Out_time)

    while True:
        schedule.run_pending()
        time.sleep(1)   


if __name__ == "__main__":
    main()