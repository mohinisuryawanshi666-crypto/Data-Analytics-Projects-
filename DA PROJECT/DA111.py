
import pandas as pd

df = pd.DataFrame({
    'Name': ['Komal', 'Luiza', 'Dipati', 'rameshwari', 'Isha'],
    'Age': [27, 26, 22, 21, 25],
    'Department': ['computer science', 'IT', 'Cyber Security', 'IT', 'Mechanical'],
    'Salary': [100000, 900000, 78000, 96000, 88000]
}) 

print("Original Data:", df)
print("\nSubset (salary>50):", df[df['Salary'] > 50])
print("\nSorted by Salary (Ascending):\n", df.sort_values("Salary"))
print("\nSorted by Salary (Descending):\n", df.sort_values("Salary", ascending=False))


print("\nGrouped (Average Salary by Department):\n", df.groupby("Department")["Salary"].mean())

print("\nMean =", df["Salary"].mean())
print("Median =", df["Salary"].median())

print("Mode =")
print(df["Salary"].mode())

