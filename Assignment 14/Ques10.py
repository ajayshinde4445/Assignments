print("-" * 50)
print("lambda function accept 3 number and return largest Number")
print("-" * 50)

LargestX = lambda no1,no2,no3: no1 if (no1 > no2 and no1 > no3) else (no2 if no2 > no3 else no3)

def main():
    no1 = int(input("Enter Number1 :"))
    no2 = int(input("Enter Number2 :"))
    no3 = int(input("Enter Number3 :"))


    Ret = LargestX(no1,no2,no3)

    print(f"Largest number of {no1} and {no2} and {no3} is :",Ret)

if __name__ == "__main__":
    main()


