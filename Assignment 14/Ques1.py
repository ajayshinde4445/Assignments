print("---------------------------------------")
print("------Lambda function accepts one number"
" return Sqaure--------")
print("---------------------------------------")


SqaureX = lambda no:no * no

def main():
    Value = int(input("Enter The number :"))

    Ret = SqaureX(Value)

    print(f"Square of {Value} is : ",Ret)

if __name__ == "__main__":
    main()
