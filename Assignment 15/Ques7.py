print("-" * 50)
print("lambda function using filter() accept list() of String and return list of odd Strings having length greter than 5")
print("-" * 50)


greterX = lambda x:len(x) > 5
    

def main():
    words = ["Apple","banana","Cherry","fig","kiwi"]

    long_words = list(filter(greterX,words))

    print(long_words)

if __name__ == "__main__":
    main()