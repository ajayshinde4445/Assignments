def NumDigit(no):
    cnt = 0
    while(no > 0):
        no % 10
        cnt +=1
        no //= 10
    
    return cnt

def main():
    value = int(input("Enter The number :"))

    ret = NumDigit(value)
    print(ret)

if __name__ == "__main__":
    main()