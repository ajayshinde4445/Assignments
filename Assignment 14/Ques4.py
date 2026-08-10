print("------------------------------------------")
print("lambda function accepts two number and return minimum")
print("------------------------------------------")

MinX = lambda no1,no2:no1 > no2

def main():
     no1 = int(input("Enter First Number :"))
     no2 = int(input("Enter Second Number :"))

     Ret = MinX(no1,no2)

     if Ret == False:
          print(f"{no1} is minimum number")
     else:
          print(f"{no2} is minimum number")

if __name__ == "__main__":
     main()