print("--------------------------------------------------")
print("---------Accept mark and display grade---------------")
print("--------------------------------------------------")


def GradeMark(no):
    if no >= 75 :
        print("Your in Distinction")
    elif no >= 60:
        print("Your in First Class")
    elif no>=50:
        print("Your in Second Class")
    elif no < 50:
        print("Your Are Fail")





def main():
    Marks = int(input("Enter The Number :"))

    GradeMark(Marks)

if __name__ == "__main__":
    main()

