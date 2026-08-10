# write a prog which accept one character and check whether 
# it is vowel or consonant

def VowelX(x):
    if (x == 'a' or x == 'A' or
        x == 'e' or x == 'E' or
        x == 'i' or x == 'I' or
        x == 'o' or x == 'O' or
        x == 'u' or x == 'U'):
        print("Character is Vowel")
    else:
        print("Character is consonant")
        

def main():
    word = input("Enter One character :")

    VowelX(word)
if __name__ == "__main__":
    main()