# write prog accept number and print sum of digit

def SumDigit(no):
    ans = 0

    while no > 0:
        sum = no % 10
        ans = ans + sum
        no //= 10   
    return ans     

def main():
    value = int(input("Enter the number :"))
    
    ret = SumDigit(value)
    print("Sum of Digit :",ret)

if __name__ == "__main__":
    main()