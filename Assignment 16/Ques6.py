print("-" * 70)
print("Write prog which display number is positive ,negative or zero")
print("-" * 70)

def ChkNum(no):
    if no == 0:
        print("Zero")
    elif no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")

def main():

    no = int(input("Enter Number :"))

    ChkNum(no)

if __name__ == "__main__":
    main()