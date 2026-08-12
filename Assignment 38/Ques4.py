import pandas as pd

def main():
    border = "-"*40

    Dataset ="student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print(border)
    # print(df['FinalResult'].value_counts())

    print("Pass Student Percentage :")
    print(df['FinalResult'].value_counts(normalize=1)*100)

if __name__ == "__main__":
    main()