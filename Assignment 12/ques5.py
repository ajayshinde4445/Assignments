# write a prog accept number and print till that number reverse

def ReverseDigit(no):
    while(no>0):
        ans = no % 10
        print(ans,end=" ")
        no = no//10
def main():
    value = int(input("Enter the number :"))

    ReverseDigit(value)

if __name__ == "__main__":
    main()
