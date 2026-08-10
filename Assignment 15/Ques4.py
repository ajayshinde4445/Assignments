from functools import reduce

print("-" * 50)
print("lambda function using reduce() accept list() of number and return list of Addition of all number")
print("-" * 50)

additionX = lambda x,y: x+y

def main():
    a = [2, 4, 6, 8]
    # r = reduce(lambda x, y: x + y, a)

    r = reduce(additionX,a)
    print(r)

if __name__ == "__main__":
    main()