print("-" * 70)
print("Write prog which contain one function named as ChkNum().that function accept one paramter as number."
"if number even it should display Even number else odd number")
print("-" * 70)

def EvenOdd(no):
    if no % 2 == 0:
        print("Even Number ")
    else:
        print("Odd Number ")

def main():
    value = int(input("Enter The Number :"))

    EvenOdd(value)

if __name__ == "__main__":
    main()