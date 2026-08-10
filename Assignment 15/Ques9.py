print("-" *50)
print("lambda using Reduce accept list of number and return product of all number")
print("-" *50)

from functools import reduce

ProdX = lambda x,y:x * y
    

def main():
    Data = [1,2,3,4,5]

    Ret = reduce(ProdX,Data)

    print("Product of all list : ",Ret)

if __name__ == "__main__":
    main()