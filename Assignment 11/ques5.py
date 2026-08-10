# write a prog accept number and check it is palindrom or not
def PalindromX(no):
    if no < 0 or (no % 10 == 0 and no != 0):
        return False
    
    orinalNum = no
    rev_num = 0

    while no>0:
        digit = no % 10
        rev_num = (rev_num * 10) + digit
        no = no // 10

    if orinalNum == rev_num:
        print("Number is palindrom")
    else:
        print("Nunber is Not Palindrom")



def main():
    value = int(input("Enter Number :"))

    PalindromX(value)


if __name__ == "__main__":
    main()