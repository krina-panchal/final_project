# Importing necessary data analysis and visualisation Python libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset using Pandas
# Note: Update the file path based on the location of the attp_data.xlsx file
appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

# Data Visualisation

# Bar chart of the count of applicants by Ethnicity Group
plt.figure(figsize=(20, 10))

# Getting unique values for the 'Gender' column
genders = appt_data['Gender'].unique()

# Creating bars for each gender
bar_width = 0.35  # Adjust this value as needed
for i, gender in enumerate(genders):
    gender_data = appt_data[appt_data['Gender'] == gender]
    ethnic_group_counts = gender_data['Ethnic Group'].value_counts()
    
    # Plotting each bar
    plt.bar(
        x=range(len(ethnic_group_counts)) if i == 0 else [pos + bar_width for pos in range(len(ethnic_group_counts))],
        height=ethnic_group_counts,
        width=bar_width,
        label=gender,
        color='lightblue' if gender == 'Male' else 'pink'
    )

# Customising the plot labels and title
plt.xlabel('Ethnicity Group')
plt.ylabel('Count')
plt.title('Distribution of Applicants by Ethnicity Group and Gender')

# Adding x-axis labels for each ethnic group
plt.xticks(ticks=[pos + bar_width / 2 for pos in range(len(ethnic_group_counts))], labels=ethnic_group_counts.index)

plt.legend()
plt.show()

