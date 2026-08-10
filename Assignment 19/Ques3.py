from functools import reduce
contain = lambda no:no>=70 and no<=90
increse = lambda no:no+10
Product = lambda x,y:x * y 

def main():
    size = int(input("Enter the size :"))
    
    data = list()

    print("Enter Data :")

    for i in range(size):
        no =int(input())
        data.append(no)

    print(data)

    Fdata = list(filter(contain,data))
    Mdata = list(map(increse,Fdata))
    # Rdata = reduce(lambda x,y:x+y,Mdata)
    Rdata = reduce(Product,Mdata)

    print("After Filter :",Fdata)
    print("After Map:",Mdata)
    print("After Reduce :",Rdata)

if __name__ == "__main__":
    main()