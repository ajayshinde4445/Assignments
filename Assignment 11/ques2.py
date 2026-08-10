# write prog accept one number and print count of digit

def CountDigit(no):
    ans = 0

    while no > 0:
        # sum = no % 10
        no //= 10
        ans = ans + 1

        
    return ans     

def main():
    value = int(input("Enter the number :"))
    
    ret = CountDigit(value)
    print("count of Digit :",ret)

if __name__ == "__main__":
    main()