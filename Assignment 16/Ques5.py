print("-" * 70)
print("Write prog which display 10 to 1 on screen")
print("-" * 70)

def DisplayReverse():
    for i in range(10,0,-1):
        print(i,end="   ")

def main():
    DisplayReverse()

if __name__ == "__main__":
    main()