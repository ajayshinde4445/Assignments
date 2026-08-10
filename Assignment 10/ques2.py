# ques 2:
# write a prog which accept one number and print sum of first n natural number

def NaturalSum(no):
    sum=0

    for i in range(no+1):
        sum=sum+i

    return sum

def main():
    no = int(input("Enter number :"))

    ret = NaturalSum(no)
    print("Sum Of natural number :",ret)

if __name__ == "__main__":
    main()