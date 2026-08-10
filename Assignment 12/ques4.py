# write prog which accept one number 
# and print that number starting from 1 eg i/p:5 o/p: 12345

def AllDigit(no):
    for i in range(1,no+1):
        print(i , end=" ")
def main():
    value = int(input("Enter Number :"))
    AllDigit(value)

if __name__ == "__main__":
    main()