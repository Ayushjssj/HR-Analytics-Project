import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/hr_data.csv")

# Total employees
print("Total Employees:", len(df))

# Attrition count
print("\nAttrition Count:")
print(df["Attrition"].value_counts())

# Attrition Distribution
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition Distribution")
plt.show()

# Department vs Attrition
sns.countplot(x="Department", hue="Attrition", data=df)
plt.title("Department vs Attrition")
plt.xticks(rotation=20)
plt.show()

# Gender vs Attrition
sns.countplot(x="Gender", hue="Attrition", data=df)
plt.title("Gender vs Attrition")
plt.show()

# Overtime vs Attrition
sns.countplot(x="OverTime", hue="Attrition", data=df)
plt.title("OverTime vs Attrition")
plt.show()

# Monthly Income vs Attrition
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df)
plt.title("Monthly Income vs Attrition")
plt.show()

# Age Distribution
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Export cleaned dataset
df.to_csv("../output/cleaned_hr_data.csv", index=False)

print("EDA completed and cleaned dataset exported!")