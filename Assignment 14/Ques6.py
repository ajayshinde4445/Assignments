print("-" * 20)
print("lambda function accept number and return true if number is Odd otherwise false")
print("-" * 20)

OddX = lambda no:no % 2 != 0

def main():
    no = int(input("Enter the number :"))

    Ret = OddX(no)

    print(f"{no} is Odd ? :",Ret)

if __name__ == "__main__":
    main()