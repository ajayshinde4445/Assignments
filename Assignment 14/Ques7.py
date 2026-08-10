print("-" * 50)
print("lambda function accept number and return true if number is divisible by 5 otherwise false")
print("-" * 50)

DivisibleX = lambda no:no % 5 == 0

def main():
    no = int(input("Enter the number :"))

    Ret = DivisibleX(no)

    print(f"{no} is Divisible by 5 ? :",Ret)

if __name__ == "__main__":
    main()