# Histogram of StudyHours

import pandas as pd
import matplotlib.pyplot as plt

def main():
    Dataset ="student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    df['StudyHours'].plot(
        kind='hist',
        bins=10,
        edgecolor = 'black',
        color = 'skyblue'
    )

    plt.title("Distribution Of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Frequncy")
    plt.show()

if __name__ == "__main__":
    main()