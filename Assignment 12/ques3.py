# write a prog accept two number and 
# print addition,substraction,multiplication, division

def AdditionX(no1,no2):
    ans = no1 + no2
    print("Addition is : ",ans)

def SubstractionX(no1,no2):
    if no1 > no2:
        ans = no1 - no2
        print("Substraction is :",ans)
    else:
        ans = no2 - no1
        print("substraction is :",ans)

def MultiplicationX(no1,no2):
    ans = no1 * no2
    print("Multiplication is :",ans)

def DivisionX(no1,no2):
        if no1 > no2:
            ans = no1 / no2
            print("Division is :",ans)
        else:
            ans = no2 /no1
            print("division is :",ans)

def main():
    value1 = int(input("Enter Number First :"))
    value2 = int(input("Enter Second number :"))
    AdditionX(value1,value2)
    SubstractionX(value1,value2)
    MultiplicationX(value1,value2)
    DivisionX(value1,value2)


if __name__ == "__main__":
    main()