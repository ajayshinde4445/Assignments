# write a prog which accept number and reverse that number

def ReverseX(no):
    while no > 0:
            temp = no % 10
            print(temp,end="")
            no //= 10

def main():
    value = int(input("Enter number :"))

    ReverseX(value)

if __name__ == "__main__":
    main()