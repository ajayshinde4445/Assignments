# from sklearn.datasets import student_performance_ml
import pandas as pd

def main():

    border = "-"*40
    print("Student Classification")
    print(border)
    Dataset = "student_performance_ml.csv"


    # print(Dataset)

    df = pd.read_csv(Dataset)

   #  print(df)
    print(border)
    print("First 5 Record :")
    print(border)
    print(df.head())
    print(border)

    print("Last 5 Record :")
    print(border)
    print(df.tail())
    

    print(border)
    print("Total number of rows and columns :")
    print(border)
    print(df.shape)

    print(border)
    print("List of Column Names :")
    print(border)
    print(df.columns)

    print(border)
    print("Data Types of each Column :")
    print(border)
    print(df.dtypes)
    print(border)



    


if __name__ == "__main__":
    main()