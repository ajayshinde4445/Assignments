print("-"*70)
print("Accept n number from user and store it into list " \
"return addition of all prime number from list")
print("-"*70)

import MarvellousNum

def main():
    size = int(input("Enter Number :"))

    data = list()

    print("Enter The Data")
    for i in range(size):
        no = int(input())
        data.append(no)  

    print("Data :",data)

    MarvellousNum.ChkPrime(data)
    # print("min of elemnts is :",ans)


if __name__ == "__main__":
    main()