print("-" * 70)
print("Write prog function accept one number " \
"return true if it is divisible by 5 otherwise false")
print("-" * 70)

def DivisibleX(no):
    return no % 5 == 0

def main():
    no = int(input("Enter The Number :"))

    Ret = DivisibleX(no)

    print(Ret)

if __name__ == "__main__":
    main()