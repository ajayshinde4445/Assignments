# write a prog which accept number and print all even number till that number

def EvenX(no):
    for i in range(1,no+1):
        if i%2 == 0:
            print(i , end=" ")
        
def main():

    value1 = int(input("Enter the number: "))

    EvenX(value1)

if __name__ == "__main__":
    main()