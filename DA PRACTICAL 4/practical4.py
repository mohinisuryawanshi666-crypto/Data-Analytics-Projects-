
import pandas as pd

n = int(input("Enter the number of students: "))

names = []
ages = []
depts = []
dates = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dept = input("Enter department: ")
    date = input("Enter Admission date (YYYY-MM-DD): ")

    names.append(name)
    ages.append(age)
    depts.append(dept)
    dates.append(date)

data = {
    'Name': names,
    'Age': ages,
    'Department': depts,
    'Admission_Date': dates
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

print("\nOriginal Data Types:")
print(df.dtypes)

df['Age'] = df['Age'].astype(int)
df['Name'] = df['Name'].str.strip()
df['Department'] = df['Department'].str.title()

df['Admission_Date'] = pd.to_datetime(
    df['Admission_Date'],
    format='%Y-%m-%d'
)

df['Year'] = df['Admission_Date'].dt.year
df['Month'] = df['Admission_Date'].dt.month
df['Day'] = df['Admission_Date'].dt.day

print("\nTransformed Data:")
print(df)

print("\nTransformed Data Types:")
print(df.dtypes)

