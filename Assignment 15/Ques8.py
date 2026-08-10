print("-" *50)
print("lambda using filter accept list of number and return divisible by 3 and 5")
print("-" *50)




DivisibleX = lambda no:no % 3 == 0 and no % 5 == 0

def main():
    Data = [20,22,45,77,12,15]

    Ret = list(filter(DivisibleX,Data))

    print("Divisible by 3 and 5 :",Ret)

if __name__ == "__main__":
    main()