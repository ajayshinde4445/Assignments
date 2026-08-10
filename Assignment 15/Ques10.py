print("-" *50)
print("lambda using filter accept list of number and return count of Even number")
print("-" *50)

EvenCount = lambda no : no % 2 == 0

def main():
    Data = [12,22,10,34,33,75,66]

    Ret = len(list(filter(EvenCount,Data)))

    print("Total Even number :",Ret)

if __name__ == "__main__":
    main()
