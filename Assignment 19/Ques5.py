from sympy import isprime
from functools import reduce

def PrimeX(data):

    pData = isprime(data)

MultiX = lambda no : no * 2

def MaximumX(a):
    res = a[0]

    for i in a:
        if i > res:
            res = i
    return res

def main():
    size = int(input("Enter the size :"))
    
    data = list()

    print("Enter Data :")

    for i in range(size):
        no =int(input())
        data.append(no)

    print(data)

    Fdata = list(filter(PrimeX,data))
    Mdata = list(map(MultiX,Fdata))
    # Rdata = reduce(lambda x,y:x+y,Mdata)
    Rdata = reduce(MaximumX,Mdata)

    print("After Filter :",Fdata)
    print("After Map:",Mdata)
    print("After Reduce :",Rdata)

if __name__ == "__main__":
    main()