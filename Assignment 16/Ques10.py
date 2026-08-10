print("-" * 70)
print("Write prog function accept name and display lenght of its name")
print("-" * 70)

def LenDis(data):
    print(len(data))

def main():
    name = input("Enter Your Name :")

    LenDis(name)

if __name__ == "__main__":
    main()