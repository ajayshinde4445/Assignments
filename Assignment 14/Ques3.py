print("-----------------------------------")
print("Lambda Function Accept two number return Max Number")
print("-----------------------------------")

MaxX = lambda no1,no2:no1 > no2

def main():
     no1 = int(input("Enter First Number :"))
     no2 = int(input("Enter Second Number :"))

     Ret = MaxX(no1,no2)

     if Ret == True:
          print(f"{no1} is maximum number")
     else:
          print(f"{no2} is maximum number")

if __name__ == "__main__":
     main()