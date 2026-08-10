def NumberX(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end=" ")
            # print("*",end=" ")
        print()
def main():
    value = int(input("Enter The number :"))

    NumberX(value)

if __name__ == "__main__":
    main()