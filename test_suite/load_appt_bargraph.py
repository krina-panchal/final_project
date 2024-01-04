# Importing all necessary  Python data visualisation and analysis libraries
import pandas as pd
import matplotlib.pyplot as plt

# Bar chart of the count of applicants by Ethnicity Group
def create_ethnicity_gender_plot(appt_data):
    """
    Create a bar chart depicting the count of applicants by Ethnicity Group and Gender.

    Parameters:
    - appt_data (DataFrame): Pandas DataFrame containing the data.

    Returns:
    - fig (Figure): Matplotlib Figure object representing the created plot.
    """
    fig, ax = plt.subplots(figsize=(20, 10))

    # Getting unique values for the 'Gender' column
    genders = appt_data['Gender'].unique()

    # Creating bars for each gender
    bar_width = 0.35 
    for i, gender in enumerate(genders):
        gender_data = appt_data[appt_data['Gender'] == gender]
        ethnic_group_counts = gender_data['Ethnic Group'].value_counts()
        
        # Sort ethnic groups alphabetically
        ethnic_group_counts = ethnic_group_counts.sort_index()

        # Plotting each bar
        ax.bar(
            x=range(len(ethnic_group_counts)) if i == 0 else [pos + bar_width for pos in range(len(ethnic_group_counts))],
            height=ethnic_group_counts,
            width=bar_width,
            label=gender,
            color='lightgreen' if gender == 'Male' else 'lightpink'
        )

    # Customising the plot labels and title
    ax.set_xlabel('Ethnicity Group')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Applicants by Ethnicity Group and Gender')

    # Adding x-axis labels for each ethnic group
    ax.set_xticks([pos + bar_width / 2 for pos in range(len(ethnic_group_counts))])
    ax.set_xticklabels(ethnic_group_counts.index)

    ax.legend()
    return fig

if __name__ == "__main__":
    
    appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")
    create_ethnicity_gender_plot(appt_data)
    plt.show()
