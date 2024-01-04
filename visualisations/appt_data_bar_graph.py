# Importing necessary data analysis and visualisation Python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset using Pandas
# Note: Update the file path based on the location of the attp_data.xlsx file
appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

# Data Visualisation

#Bar chart of the count of applicants by Ethnicity Group
# Creating a new figure with a specified size
plt.figure(figsize=(20, 10))

# Use Seaborn to create a count plot
sns.countplot(x='Ethnic Group', data=appt_data, hue='Gender', palette={'Male': 'lightblue', 'Female': 'pink'})

# Customising the plot labels and title
plt.xlabel('Ethnicity Group')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Ethnicity Group and Gender')

# Add legend to show the hue (Gender)
plt.legend()

# Displays the plot
plt.show()
