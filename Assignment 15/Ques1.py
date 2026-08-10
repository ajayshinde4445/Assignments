SqaureX = lambda no : no * no

def main():
    data = [11,2,5,7,10,12]
    print("List :",data)

    Result = list(map(SqaureX,data))

    print(Result)

if __name__ == "__main__":
    main()