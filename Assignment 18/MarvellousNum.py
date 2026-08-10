def ChkPrime(data):
    # print("inside fun")
    ans=0
    for i in data:
        # print("Inside loop")
        for n in range(2,i+1):
            # print("inner loop")
            if i % n  ==0:
                ans = ans + i
                print(ans)
        # return ans
