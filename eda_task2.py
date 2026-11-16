import pandas as pd
import numpy as np
df=pd.read_csv("students.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df[["Math", "English", "Science"]].corr())
