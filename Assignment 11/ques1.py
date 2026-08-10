# write a prog which accept one number and display it is prime or not

def ChkPrimeX(no):
    if no>1:
        for i in range(2,no):
            if no % i == 0:
                print("Number is not a prime")
                break
        else:
            print("number is a prime")
    else:
        print("number is not a prime")



def main():
    value = int(input("Enter Number :"))

    ChkPrimeX(value)

if __name__ == "__main__":
    main()