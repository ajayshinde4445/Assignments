print("-"*70)
print("print namaskar everyday at 9.00am min")
print("-"*70)
import datetime
import schedule
import time
def Display():
    print("Namaskar...")


def main():
    print("Automation Script Started")

    schedule.every(1).day.at("13:35").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(10)

    print("Automation Script End")
    

if __name__ == "__main__":
    main()

