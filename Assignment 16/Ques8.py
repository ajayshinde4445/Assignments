print("-" * 70)
print("Write prog function accept one number and print that number of * on screen")
print("-" * 70)

def StarX(no):
    for i in range(no):
        print("*",end=" ")

def main():
    no = int(input("Enter Number :"))
    StarX(no)

if __name__ == "__main__":
    main()