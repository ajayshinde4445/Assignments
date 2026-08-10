import time
import threading
print("-" *70)
print("Create two separate threads named Thread1 display 1 -50  and Thread2 display 50 - 1 thread run after 1st thread")
print("-"*70)

def PrimeX(Value1):

    
    for i in range(2, int(Value1**0.5) + 1):
        if Value1 % i == 0:
            return False
        return True

        

def Dis_Prime(no):
   primes=[]
   for num in no:
       if PrimeX(num):
           primes.append(num)
           print(f"Prime number found :{primes}\n",end="")

def dis_nonprime(no):
    non_prime = []
    for num in no:
        if not PrimeX(num):
            non_prime.append(num)
    print(f"non-prime number :{non_prime}\n",end="")
        
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
    obj1= threading.Thread(target=PrimeX,args=(data,))
    # obj2= threading.Thread(target=NonPrime,args=(data,))


    obj1.start()
    obj1.join()

 



    # obj2.start()
    # obj2.join()


    print()
    print("-"*20)


    # print(f"Total Time required :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()