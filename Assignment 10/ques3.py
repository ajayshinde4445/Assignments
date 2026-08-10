# write a program which accept one number and prints factorial of that number

def FactoraialX(no):
    ans =1
    for i in range(1,no+1):
        
        ans = ans * i
    return ans
        
def main():
    a = int(input("Enter the number :"))

    ret = FactoraialX(a)

    print("Factorial is :",ret)


if __name__ == "__main__":
    main()