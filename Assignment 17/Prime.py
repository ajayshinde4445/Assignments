def PrimeNum(no):
    for i in range(2,no+1):
        if no % i == 0:
            print(f"number {no} is prime")
        else:
            print(f"number {no} is not prime")

