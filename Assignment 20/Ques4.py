import time
import threading

def Small(value1):
    print("Thread Id :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    scnt=0
    for i in value1:
        if i.islower():
            scnt = scnt+1
    print("Lower Char In string is :",scnt)
    

def Capital(value2):
    print("Thread Id :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)


    ucnt=0
    for i in value2:
        if i.isupper():
            ucnt = ucnt+1
    print("Upper Char In string is :",ucnt)

def Digits(value3):
    print("Thread Id :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)


    dcnt=0
    for i in value3:
        if i.isdigit():
            dcnt = dcnt+1
    print("Digit In string is :",dcnt)
    

def main():
    value = input("Enter The String :")

    start_time = time.perf_counter()

    obj1 = threading.Thread(target=Small,args=(value,))
    obj2 = threading.Thread(target=Capital,args=(value,))
    obj3 = threading.Thread(target=Digits,args=(value,))

    obj1.start()
    obj2.start()
    obj3.start()

    obj1.join()
    obj2.join()
    obj3.join()


    end_time = time.perf_counter()

    print(f"Total Time :{end_time - start_time:.4f}")



if __name__ == "__main__":
    main()