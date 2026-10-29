import pandas as pd

df = pd.DataFrame({
    'Name': ['Mohini', 'Zunera', 'KAruna', 'Devyanshi', 'Isha'],
    'Age': [20, 20, 22, 21, 20],
    'Department': ['computer science', 'IT', 'Cyber Security', 'IT', 'Mechanical'],
    'Marks': [85, 92, 78, 96, 88]
}) 

print("Original Data:", df)
print("\nSubset (marks>50):", df[df['Marks'] > 50])
print("\nSorted by Marks (Ascending):\n", df.sort_values("Marks"))
print("\nSorted by Marks (Descending):\n", df.sort_values("Marks", ascending=False))


print("\nGrouped (Average Marks by Department):\n", df.groupby("Department")["Marks"].mean())

print("\nMean =", df["Marks"].mean())
print("Median =", df["Marks"].median())

print("Mode =")
print(df["Marks"].mode())

