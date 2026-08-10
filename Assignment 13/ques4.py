def DecBin(no):
    res = " "

    while no > 0:
        res = str(no % 2) + res
        no = no // 2

    return res

def main():
    value = int(input("Enter the Number :"))

    ret = DecBin(value)
    print(ret)

if __name__ == "__main__":
    main()