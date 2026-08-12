import pandas as pd
# 1.Total number of student in the dataset
# 2.Count how many student passed(final result =1)
# 3.Count how many failed(final result =0)

def main():
    border = "-"*40
    print("Student Performance Classification")

    Dataset = "student_performance_ml.csv"
    df = pd.read_csv(Dataset)


    print(border)
    print("Total Number of Student :",df.shape[0])
    # print(len(df))    Same as above o/p

    pass_count = len(df[df["FinalResult"] == 1])
    print("Total Passed Students :",pass_count)

    fail_count = len(df[df["FinalResult"] == 0])
    print("Total failed Student :",fail_count)



if __name__ == "__main__":
    main()
