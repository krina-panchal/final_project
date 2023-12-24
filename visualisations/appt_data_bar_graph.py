import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset using Pandas
appt_data = pd.read_excel('appt_data.xlsx')

# Data Visualisation

#Count of Applicants by Gender
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=appt_data)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Gender')
plt.show()

#Bar chart of the count of applicants by Ethnicity Group
plt.figure(figsize=(12, 8))
sns.countplot(x='Ethnicity Group', data=appt_data, hue='Gender')
plt.xlabel('Ethnicity Group')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Ethnicity Group and Gender')
plt.legend()
plt.show()

#Age distribution of applicants
plt.figure(figsize=(12, 8))
sns.histplot(x='Age', data=appt_data, bins=20, kde=True)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution of Applicants')
plt.show()

#Stacked bar chart of applicants by Level and Industry
plt.figure(figsize=(14, 8))
sns.countplot(x='Level', hue='Industry', data=appt_data)
plt.xlabel('Level')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Level and Industry')
plt.legend(title='Industry', loc='upper right')
plt.show()
