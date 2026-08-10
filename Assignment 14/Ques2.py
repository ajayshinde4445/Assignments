print("------------------------------------------------")
print("Write lambda function accept one number "
"and return Cube of that number")
print("------------------------------------------------")

CubeX=lambda no:no ** 3

def main():
    value = int(input("Enter The Number :"))

    Ret = CubeX(value)

    print(f"Cube of {value} is :",Ret)

if __name__ == "__main__":
    main()