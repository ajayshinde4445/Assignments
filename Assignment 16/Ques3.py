print("-" * 70)
print("Write prog which contain one function named as Add().that function accept two paramter as number."
"display its addition")
print("-" * 70)

def AdditionX(no1,no2):
    ans = no1 + no2

    print("Addition is :",ans)

def main():
    no1 = int(input("Enter First Number :"))
    no2 = int(input("Enter First Number :"))

    AdditionX(no1,no2)

if __name__ == "__main__":
    main()

