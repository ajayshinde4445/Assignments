import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Dataset ="student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    # initilise plot figsize
    plt.figure(figsize=(8,6))

    print(df.columns)
    print(df.head())
    print(df.dtypes)

    # create scatter plot

    sns.scatterplot(
    data=df,
    x='StudyHours',
    y='Attendance',
    hue='FinalResult',
    palette='viridis',
    s=100,
    edgecolor='black'
    )


    # Add label and titile
    plt.title("Relation Between StudyHours and PreviousScore")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")

    # display grid and plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()



if __name__ == "__main__":
    main()