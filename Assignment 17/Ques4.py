print("-"*70)
print("accept number from user and return additio of its factorial")
print("-"*70)

import AddFact

def main():
    no = int(input("Enter The Number :"))

    ret = AddFact.AddFact(no)

    print("Addition of Factorial :",ret)

if __name__ == "__main__":
    main()