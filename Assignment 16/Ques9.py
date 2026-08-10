print("-" * 70)
print("Write prog function display first 10 even number")
print("-" * 70)

def EvenDis():
    cnt = 0
    number = 2

    while cnt < 10:
        if number % 2 == 0:
            print(number, end=" ")
            cnt += 1

        number += 1

def main():
    print("Display first even number :")
    EvenDis()

if __name__ == "__main__":
    main()