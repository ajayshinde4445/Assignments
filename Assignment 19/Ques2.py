print("-"*70)
print("Contain lambda function which accept two paramter and return power of two")
print("-"*70)

PowerX=lambda no1,no2:no1 * no2

def main():
    no1 = int(input("Enter the first Number :"))
    no2 = int(input("Enter the second Number :"))


    ret = PowerX(no1,no2)

    print(f"Multiplication of {no1} and {no2} is :",ret)

if __name__ == "__main__":
    main()