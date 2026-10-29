
import pandas as pd

# Function to calculate average salary
def calculate_average(salary_list):
    return sum(salary_list) / len(salary_list)


names = ["Mohini", "Priya", "Rahul", "Zunera", "Amit"]
salary = [1300000, 850000, 600000, 1500000, 950000]


df = pd.DataFrame({
    "Name": names,
    "Salary": salary
})

def result(salary):
    if salary >= 1250000:
        return "higher package"
    elif salary >= 750000:
        return "average package"
    else:
        return "low package"


df["Result"] = df["Salary"].apply(result)

print("\nDataset:")
print(df)

print("\nEmployee Analysis:")
for current_salary in salary:
    if current_salary >= 1250000:
        print(current_salary, "higher package")
    elif current_salary >= 750000:
        print(current_salary, "average package")
    else:
        print(current_salary, "low package")


print("\nAverage Salary:", calculate_average(salary))
print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))
