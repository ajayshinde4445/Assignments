import time
import threading
print("-"*70)
print("Create two separate threads named Even factor and Odd factor and sum of that both")
print("-"*70)

def EvenFact(no):
    Esum = 0
    for i in range(2,no+1,2):
        print(i,end=" ")
        # if no % i == 0:
        Esum = Esum + i
    print()
    print(f"Sum of Even Factor of Given Number {no} :",Esum)
  



        
def OddFact(no):
    sum = 0
    for i in range(1,no+1,2):
        print(i,end=" ")
        # if no % i == 0:
        sum = sum + i
    print()
    print(f"Sum of Odd Factor of Given Number {no} :",sum)
    
        

def main():
    start_time = time.perf_counter()

    print("Start Time",start_time)

    print("-"*20)
    obj1= threading.Thread(target=EvenFact,args=(20,))
    obj2= threading.Thread(target=OddFact,args=(20,))

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