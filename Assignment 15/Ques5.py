from functools import reduce

print("-" * 50)
print("lambda function using reduce() accept list() of number and return list of maximum of all number")
print("-" * 50)

MultiX = lambda x,y: x>y

def main():
    a = [2, 4, 6, 8]

    print("Data :",a)
    # r = reduce(lambda x, y: x + y, a)

    r = reduce(MultiX,a)
    print(r)

if __name__ == "__main__":
    main()