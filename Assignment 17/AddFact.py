def AddFact(no):
    sum=0

    for i in range(1,no):
        if no % i == 0:
            sum = sum + i

    return sum