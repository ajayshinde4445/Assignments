def FactX(no):
    for i in range(1,no+1):
        if no % i ==0:
            print(i ,end=" ")

def main():
    no = int(input("Enter the Number :"))

    FactX(no)

if __name__ == "__main__":
    main()