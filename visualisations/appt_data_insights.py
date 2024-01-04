# Importing necessary data analysis and visualisation Python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Note: Update the file path based on the location of the attp_data.xlsx file
appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

# Data Visualisation

# Stacked bar chart of applicants by Level and Industry
plt.figure(figsize=(14, 8))

#creating a count plot with stacked bars
sns.countplot(x='Level', hue='Industry', data=appt_data)

# Customising the plot labels and title
plt.xlabel('Level')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Level and Industry')

# Add legend to show the hue (Industry) and customize its title and location
plt.legend(title='Industry', loc='upper right')

# Display the plot
plt.show()
