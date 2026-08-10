print("-"*70)
print("print jay ganesh every 1 min")
print("-"*70)
import datetime
import schedule
import time
def Display():
    print("Jay Ganesh...")


def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("Automation Script End")
    

if __name__ == "__main__":
    main()

