def OccWord(file,word):
    count = 0

    fobj = open(file,"r")

    for line in fobj:
        words = line.split()
        for i in words:
            if(i == word):
                count+=1
    return count


def main():
    file_name = input("Enter the file name or path: ")
    word = input("Enter Word  to find :")

    Ret = OccWord(file_name,word)

    print(f"Occurrence {word} Word in total :",Ret)
    
if __name__ == "__main__":
    main()