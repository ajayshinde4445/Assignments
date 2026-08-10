def EvenFact(no):
    sum = 0
    Edata = list()
    for i in range(2,no+1,2):
        print(i)
        Edata.append(i)
    for i in Edata:
        no % i == 0
        sum = sum + i
    print(sum)


        

        

def main():
    EvenFact(10)

if __name__ =="__main__":
    main()