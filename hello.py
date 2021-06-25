import pandas as pd

df=pd.read_csv("Employee_Salary_Dataset.csv")

print(df.head(10))
print(df.corr())
