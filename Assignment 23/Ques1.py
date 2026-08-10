print("-"*70)
print("list of integer and use pool.map() sum of sqaure from 1 to n for every elements in list")
print("-"*70)

from multiprocessing import pool
import time 

def SumSqaure(data):
    total = []
    sum=0
    for i in data:
        for j in range(1,i):
            no = j **2
            sum = sum+no
        total.append(sum)

    return total


    
def main():
    a = [1,2]
    with Pool() as pool:
        Ret = pool.map(SumSqaure,a)

    print("Sum of Sqaure : ",Ret)

if __name__ == "__main__":
    main()
