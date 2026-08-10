print("-"*70)
print("Accept n number from user and store it into list " \
"return Minimum of all elemnts")
print("-"*70)


def MinimumX(a):
    res = a[0]

    for i in a:
        if i < res:
            res = i
    return res


    

def main():
    size = int(input("Enter Number :"))

    data = list()

    print("Enter The Data")
    for i in range(size):
        no = int(input())
        data.append(no)  

    print("Data :",data)

    ans = MinimumX(data)
    print("min of elemnts is :",ans)


if __name__ == "__main__":
    main()