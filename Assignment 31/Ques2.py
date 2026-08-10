print("-"*70)
print("accept msg from user and display after interval time")
print("-"*70)
import datetime
import schedule
import time
def DisplayMessage(msg):
    
    print(msg)


def main():
    message = input("Enter The message to display : ")
    print("Automation Script Started")

    schedule.every(5).seconds.do(DisplayMessage,message)
    while True:
        schedule.run_pending()
        time.sleep(1)


    print("Automation Script End")
    

if __name__ == "__main__":
    main()

