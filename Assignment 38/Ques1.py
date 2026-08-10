# from sklearn.datasets import student_performance_ml
import pandas as pd

def main():
    print("Iris Classificstion Case study")
    print("_"*30)
    Dataset = "student_performance_ml.csv"

    print(Dataset)

    df = pd.read_csv(Dataset)

   #  print(df)
    print("First 5 Record",df.head())
    print("Last 5 Record",df.tail())

    print("Total number of rows and columns",df.shape)

    print("List of Column Names:",df.columns)


    # print("Column Names :",list(df.columns))


    


if __name__ == "__main__":
    main()