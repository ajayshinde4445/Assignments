print("-" * 50)
print("lambda function using filter() accept list() of number and return list of odd number")
print("-" * 50)

OddX=lambda no:no % 2 != 0
def main():
    data=[11,21,51,17,10,16]
    print("Input data is : ",data)

    Fdata=list(filter(OddX,data))
    
    print("Data after filter : ",Fdata)
if __name__ == "__main__":
    main()