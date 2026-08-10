# write a prog which accept length and width
# of rectangle and print area

# def AreaX(l,w):
    
#     return l * w

AreaX = lambda l,w:l * w


def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width :"))

    ret  = AreaX(length,width)

    print("Area of rectaingle :",ret)



if __name__ == "__main__":
    main()