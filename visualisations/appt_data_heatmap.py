import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

# Data Visualisation  
# Grouping data by 'Industry' and 'Ethnic Group', calculating the count, and unstacking the result
industry_ethnic_group_counts = appt_data.groupby(['Industry', 'Ethnic Group']).size().unstack().plot(kind='barh', stacked=True, colormap='plasma_r')

# Creating a clustered horizontal bar chart 
plt.title('Applicants by Industry and Ethnic Group')

# Labelling both axis
plt.ylabel('Industry')
plt.xlabel('Count')
# Adding legend outside the plot for clarity
plt.legend(title='Ethnic Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()