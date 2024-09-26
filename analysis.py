import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
## Loading the Data:
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

##Basic Descriptive Statistics:
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')
df['total_charges'] = df['total_charges'].str.replace('[\$,]', '', regex=True)
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = df['total_costs'].str.replace('[\$,]', '', regex=True)
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')
df_stay = df[df['length_of_stay']!="120 +"]

### Mean
mean_stay = df_stay['length_of_stay'].mean()
mean_charges = df['total_charges'].mean()
mean_costs = df['total_costs'].mean()

### Median
median_stay = df['length_of_stay'].median()
median_charges = df['total_charges'].median()
median_costs = df['total_costs'].median()

### Standard Deviation
std_stay = df['length_of_stay'].std()
std_charges = df['total_charges'].std()
std_costs = df['total_costs'].std()

### Min/Max
min_stay = df['length_of_stay'].min()
max_stay = df['length_of_stay'].max()

min_charges = df['total_charges'].min()
max_charges = df['total_charges'].max()

min_costs = df['total_costs'].min()
max_costs = df['total_costs'].max()

### Percentiles (25th, 50th, 75th)
percentiles_stay = df['length_of_stay'].quantile([0.25, 0.50, 0.75])
percentiles_charges = df['total_charges'].quantile([0.25, 0.50, 0.75])
percentiles_costs = df['total_costs'].quantile([0.25, 0.50, 0.75])

print(mean_stay, mean_charges , mean_costs)
print(median_stay, median_charges , median_costs)
print(std_stay, std_charges , std_costs)
print(min_stay, min_charges , min_costs)
print(max_stay, max_charges , max_costs)
print(percentiles_stay, percentiles_charges , percentiles_costs)

## Exploring Categorical Variables:
age_group_count = df['age_group'].value_counts()
gender_counts = df['gender'].value_counts()
type_admission_counts = df['type_of_admission'].value_counts()

print(age_group_count, gender_counts ,type_admission_counts)

plt.figure(figsize=(10, 6))
sns.countplot(x='age_group', data=df, order=df['age_group'].value_counts().index)
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['gender'], bins=2, kde=True)
plt.title('Distribution of gender')
plt.xlabel('gender')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['type_of_admission'], bins=4, kde=True)
plt.title('Distribution of type_of_admission')
plt.xlabel('type_of_admission')
plt.ylabel('Frequency')
plt.show()


## Visualizations
plt.figure(figsize=(10, 6))
sns.histplot(df['length_of_stay'], bins=20, kde=True)
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='total_charges', data=df)
plt.title('Boxplot of Total Charges')
plt.xlabel('Total Charges ($)')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='type_of_admission', data=df, order=df['type_of_admission'].value_counts().index)
plt.title('Distribution of Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.show()

## Handling Missing Data:
#### done at line 12


## Summary Report

age_group_costs = df.groupby('age_group')['total_costs'].mean()
print(age_group_costs)
type_of_admission_costs = df.groupby('type_of_admission')['total_costs'].mean()
print(type_of_admission_costs)

summary_report = """
Summary Report

1. What is the average length of stay?
- The average length of stay is approximately 5.97 days.

2. How does the total cost vary by age group or type of admission?
- By Age Group:
    As the patient's age increases, the average total cost of treatment generally rises, with the 70 or older group having the highest costs
- By Type of Admission:
  - Urgent admissions stand out as the costliest type of admission on average, with elective admissions also being relatively expensive. 
  - Emergency admissions, despite being the most common, incur lower costs on average, while newborn admissions are the least costly.

3. Any noticeable trends in admissions or charges?
- Emergency admissions dominate, suggesting a large number of patients admitted under urgent circumstances.
- Most patients are hospitalized for less than 5 days, but some stay longer.
- There are significant outliers in total charges, with a few cases exceeding $1 million, suggesting complexity and longer hospitalizations in some cases.

"""


## 
ethnicity_stats = df.groupby('ethnicity')[['total_charges', 'length_of_stay']].mean()
race_stats = df.groupby('race')[['total_charges', 'length_of_stay']].mean()

# Print the results
print("Average Total Charges and Length of Stay by Ethnicity:")
print(ethnicity_stats)

print("\nAverage Total Charges and Length of Stay by Race:")
print(race_stats)