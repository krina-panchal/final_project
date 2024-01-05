import pandas as pd
import matplotlib.pyplot as plt

def create_line_graph(df):
    # Data cleansing
    df['Year'] = df['Year'].str.extract('(\d{4}/\d{2})', expand=False)

    # Filter out rows with missing values
    filtered_data = df.dropna(subset=['Percentage'])

    # Create a line graph
    fig, ax = plt.subplots(figsize=(12, 8))

    # Iterate over unique ethnicities and plot a line for each with markers
    for ethnicity in filtered_data['Ethnicity'].unique():
        ethnicity_data = filtered_data[filtered_data['Ethnicity'] == ethnicity]
        ax.plot(ethnicity_data['Time'], ethnicity_data['Percentage'], label=ethnicity, marker='o') 

    # Customising the plot
    ax.set_title('Percentage of First-Year Enrolments by Ethnicity Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')
    ax.legend(title='Ethnicity', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load dataset
    ucas_ungrad = pd.read_csv(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_ungrad.csv")
    create_line_graph(ucas_ungrad)
