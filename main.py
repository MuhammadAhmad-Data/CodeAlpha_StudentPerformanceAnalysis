import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
print("Libraries imported successfully")
# Load dataset
df = pd.read_csv("students.csv")

# Display first 5 rows
print("\nStudent Dataset:")
print(df.head())

# Display total rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Bar Chart - Average Marks

subjects = ["Math", "English", "Science"]

average_marks = df[subjects].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    subjects,
    average_marks,
    color=["skyblue", "orange", "lightgreen"]
)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
