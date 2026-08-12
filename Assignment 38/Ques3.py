import pandas as pd
# Average StudyHours
# Average Attendance
# MAximum PreviousScore
# Minimum SleepHours

def main():
    border = "-"*40

    Dataset ="student_performance_ml.csv"
    df = pd.read_csv(Dataset)

    # # Average StudyHours
    print(border)
    Avg_Hours = (sum(df['StudyHours']))/(len(df['StudyHours']))
    print("Average StudyHours :",Avg_Hours)

    # Average Attendance
    # Attendance
    print(border)

    Avg_attendence = (sum(df['Attendance']))/(len(df['Attendance']))
    print("Average Attendance :",Avg_attendence)

    print(border)

    # MAximum PreviousScore
    # PreviousScore
    max_score = max(df['PreviousScore'])
    print("Maximum PreviousScore :",max_score)

    print(border)

    # Minimum SleepHours
    # SleepHours

    min_sleep = min(df['SleepHours'])
    print("Minimum SleepHour :",min_sleep)

    print(border)
    






if __name__ == "__main__":
    main()