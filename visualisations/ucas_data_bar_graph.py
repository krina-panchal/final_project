import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
ucas_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\ucas_data.xlsx")

# Data Visualisation

#Count of Applications by Entry Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Entry of Application', data=ucas_data)
plt.xlabel('Entry of Application')
plt.ylabel('Count')
plt.title('Count of Applications by Entry Type')
plt.show()

#Bar chart of the count of applications by Ethnic Group
plt.figure(figsize=(12, 8))
sns.countplot(x='Ethnic Group', data=ucas_data)
plt.xlabel('Ethnic Group')
plt.ylabel('Count')
plt.title('Distribution of Applications by Ethnic Group')
plt.show()

#Line chart of the number of applications over the years
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Number of Applications', data=ucas_data, marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Applications')
plt.title('Number of Applications Over the Years')
plt.show()

#Stacked bar chart of applications by Country Provider and Entry Type
plt.figure(figsize=(14, 8))
sns.countplot(x='Country Provider', hue='Entry of Application', data=ucas_data)
plt.xlabel('Country Provider')
plt.ylabel('Count')
plt.title('Distribution of Applications by Country Provider and Entry Type')
plt.legend(title='Entry of Application', loc='upper right')
plt.show()



