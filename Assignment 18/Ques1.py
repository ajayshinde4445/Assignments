print("-"*70)
print("Accept n number from user and store it into list " \
"return addition of all elemnts")
print("-"*70)


def AdditionX(a):
    res = 0
    for i in a:
        res = res +i
    
    return res

def main():
    size = int(input("Enter Number :"))

    data = list()

    print("Enter The Data")
    for i in range(size):
        no = int(input())
        data.append(no)  

    print("Data :",data)

    ans = AdditionX(data)
    print("Addition of elemnts is :",ans)


if __name__ == "__main__":
    main()