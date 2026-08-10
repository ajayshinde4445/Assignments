# write a prog accept radius and print area of circle

# def AreaCircle(r):
#     return 3.14 * r * r


AreaCircle = lambda r : 3.14 * r * r

def main():
    radius = int(input("Enter Radius of Circle :"))
    ret = AreaCircle(radius)
    print("Area of Circle :",ret)

if __name__ == "__main__":
    main()