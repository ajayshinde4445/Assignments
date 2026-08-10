print("-"*70)
print("accept msg from user and display after interval time")
print("-"*70)
import datetime
import schedule
import time
def Display(msg):
    
    print(msg)


def main():
    print("Automation Script Started")
    message = input("Enter The message to display : ")
    interval = int(input("Enter the interval in seconds: "))
    if(interval>0):
        schedule.every(interval).seconds.do(Display,message)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Interval ")

    print("Automation Script End")
    

if __name__ == "__main__":
    main()

