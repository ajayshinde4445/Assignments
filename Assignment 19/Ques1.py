print("-"*70)
print("Contain lambda function which accept two paramter and return power of two")
print("-"*70)

PowerX=lambda no:no**2

def main():
    no = int(input("Enter the Number :"))

    ret = PowerX(no)

    print(f"Power of {no} is :",ret)

if __name__ == "__main__":
    main()