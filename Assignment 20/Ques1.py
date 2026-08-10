import time
import threading
print("-"*70)
print("Create two separate threads named Even and Odd")
print("-"*70)

def Even(no):
        print("First 10 Even Number")

        for i in range(2,no+1,2):
         print(i,end=" ")

        
    
def Odd(no):
        print()
        print("First 10 Odd Number")
        for i in range(1,no,2):
             print(i,end=" ")
        

def main():
    start_time = time.perf_counter()

    print("Start Time",start_time)

    print("-"*20)
    obj1= threading.Thread(target=Even,args=(20,))
    obj2= threading.Thread(target=Odd,args=(20,))

    obj1.start()
    obj2.start()

    obj1.join()
    obj2.join()


    end_time = time.perf_counter()
    print()
    print("-"*20)

    print("End Time",end_time)

    print(f"Total Time required :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()