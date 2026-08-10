print("-" * 50)
print("lambda function accept number and return Addition")
print("-" * 50)


AdditionX = lambda no1,no2: no1 + no2

def main():
    no1 = int(input("Enter Number1 :"))
    no2 = int(input("Enter Number2 :"))

    Ret = AdditionX(no1,no2)

    print(f"Addition of {no1} and {no2} is :",Ret)

if __name__ == "__main__":
    main()