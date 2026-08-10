print("-" * 20)
print("lambda function accept number and return true if number is Even otherwise false")
print("-" * 20)

EvenX = lambda no:no % 2 == 0

def main():
    no = int(input("Enter the number :"))

    Ret = EvenX(no)

    print(f"{no} is Even ? :",Ret)

if __name__ == "__main__":
    main()