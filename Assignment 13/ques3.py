# write a prog  which accept one number and check whether it is perfect number or not

def PerfectX(no):
    sum=0
    for i in range(1,no+1):
        if no % i == 0:
            sum = sum + i
        return sum

def main():
    value = int(input("Enter the Number :"))
    ret = PerfectX(value)
    if ret == True:
        print("The number is Perfect Number")
    else:
        print("the number is not perfect number ")

if __name__ == "__main__":
    main()