print("-"*70)
print("Accept n number from user and store it into list " \
"Accept another number and check frequnecy of that number")
print("-"*70)


def FrequencyX(a,no):
    res = 0

    for i in a:
        if i == no:
            res += 1

    return res



    

def main():
    size = int(input("Enter Number :"))

    data = list()

    print("Enter The Data")
    for i in range(size):
        no = int(input())
        data.append(no)  

    print("Data :",data)

    no = int(input("Enter Freq Number :"))
    ans = FrequencyX(data,no)

    print(f"Frequncy of {no}  is :",ans)


if __name__ == "__main__":
    main()