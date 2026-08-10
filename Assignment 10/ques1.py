# ques1:
# write prog multipication table of that number

def MultiTable(no):
    # for i in range(1,11):
    #     print(i*no)
    cnt=1
    while cnt<=10:
        print(cnt * no)
        cnt = cnt+1

def main():

    a = int(input("Enter Number :"))
    MultiTable(a)

if __name__ == "__main__":
    main()