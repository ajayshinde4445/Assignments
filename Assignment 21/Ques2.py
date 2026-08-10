import time
import threading
print("-"*70)
print("Create two separate threads  Thread1 display maximum number  and Thread2 display minimum number")
print("-"*70)

def maximumX(Value1):
        res = Value1[0]
        for i in Value1:
            if i > res:
                res = i
                
        print("Maximum number :",res)
def MinimumX(Value2):
        res = Value2[0]
        for i in Value2:
            if i < res:
                res = i
        print("Minimum Number :",res)
        
def main():
    start_time = time.perf_counter()
    print("Start Time",start_time)

    Size = int(input("Enter The Size Of List :"))
    data = list()
    for i in range(Size):
        no = int(input())
        data.append(no)
    print("Display Data :",data)

    print("-"*20)
    obj1= threading.Thread(target=maximumX,args=(data,))
    obj2= threading.Thread(target=MinimumX,args=(data,))


    obj1.start()
    obj1.join()


    obj2.start()
    obj2.join()


    print()
    print("-"*20)


    # print(f"Total Time required :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()