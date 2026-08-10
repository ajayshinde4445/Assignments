import time
import threading
print("-"*70)
print("Create two separate threads named Thread1 display 1 -50  and Thread2 display 50 - 1 thread run after 1st thread")
print("-"*70)

def Thread1(no):
    for i in range(1,50+1):
        print(i,end=" ")
    print()
    print("-"*30)
    

def Thread2(no):
    for i in range(50,0,-1):
        print(i,end=" ")


        
def main():
    # start_time = time.perf_counter()

    # print("Start Time",start_time)

    print("-"*20)
    obj1= threading.Thread(target=Thread1,args=(50,))
    obj2= threading.Thread(target=Thread2,args=(50,))

    start_time1 = time.perf_counter()
    print("Start Time1",start_time1)

    obj1.start()
    obj1.join()

    end_time1 = time.perf_counter()
    print("End Time1",end_time1)


    start_time2 = time.perf_counter()
    print("Start Time2",start_time2)

    obj2.start()
    obj2.join()
    
    print()
    end_time2 = time.perf_counter()
    print("End Time2",end_time2)

    print()
    print("-"*20)


    # print(f"Total Time required :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()