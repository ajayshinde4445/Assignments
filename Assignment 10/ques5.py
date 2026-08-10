# write a prog which accept one number and print all odd number till that number

def OddX(no):
    for i in range(1,no+1):
        if i%2 != 0:
            print(i,end=" ")

def main():
    value = int(input("Enter the number :"))

    OddX(value)

if __name__ == "__main__":
    main()