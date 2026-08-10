import time
import threading
def EvenList(Elist):
    Esum = 0
    # print("Inside even")
    for i in Elist:
        # print("Inside for")
        if i % 2 == 0:
            Esum = Esum + i
    print("Sum EvenFact :",Esum)
    
def OddList(Olist):
    Osum = 0
    # print("Inside even")
    for i in Olist:
        # print("Inside for")
        if i % 2 != 0:
            Osum = Osum + i
    print("Sum EvenFact :",Osum)

def main():
    size = int(input("Enter The size of List :"))

    data = list()
    print("Enter List :")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Given List :",data)

    start_time = time.perf_counter()
    print("start time :",start_time)

    obj1 = threading.Thread(target=EvenList,args=(data,))
    obj2 = threading.Thread(target=OddList,args=(data,))


    obj1.start()
    obj2.start()

    obj1.join()
    obj2.join()
    # print("Sum EvenFact :",obj1)


    end_time = time.perf_counter()
    print("End Time :",end_time)

    print(f"Total time : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()