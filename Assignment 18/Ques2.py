print("-"*70)
print("Accept n number from user and store it into list " \
"return maximum of all elemnts")
print("-"*70)


def MaximumX(a):
    res = a[0]

    for i in a:
        if i > res:
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

    ans = MaximumX(data)
    print("max of elemnts is :",ans)


if __name__ == "__main__":
    main()