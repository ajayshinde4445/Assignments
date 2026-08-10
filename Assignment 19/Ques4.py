from functools import reduce
Even = lambda no:no % 2 == 0
Square = lambda no:no ** 2
Addition = lambda x,y:x + y 

def main():
    size = int(input("Enter the size :"))
    
    data = list()

    print("Enter Data :")

    for i in range(size):
        no =int(input())
        data.append(no)

    print(data)

    Fdata = list(filter(Even,data))
    Mdata = list(map(Square,Fdata))
    # Rdata = reduce(lambda x,y:x+y,Mdata)
    Rdata = reduce(Addition,Mdata)

    print("After Filter :",Fdata)
    print("After Map:",Mdata)
    print("After Reduce :",Rdata)

if __name__ == "__main__":
    main()