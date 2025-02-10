import pandas as pd 

def sum_value():
    df = pd.read_csv("data/SalaryData.csv")
    return df["Salary"].sum()
if __name__ == "__main__":
    print(f"Sum of salary: {sum_value()}")
    