import pandas as pd
import matplotlib.pyplot as plt

def load_and_plot_ucas_data(file_path):
    ucas_ungrad = pd.read_csv(file_path)
    ucas_ungrad['Time'] = ucas_ungrad['Time'].str.extract('(\d{4}/\d{2})', expand=False)
    filtered_data = ucas_ungrad.dropna(subset=['Percentage'])

    fig, ax = plt.subplots(figsize=(12, 8))

    for ethnicity in filtered_data['Ethnicity'].unique():
        ethnicity_data = filtered_data[filtered_data['Ethnicity'] == ethnicity]
        ax.plot(ethnicity_data['Time'], ethnicity_data['Percentage'], label=ethnicity, marker='o')

    ax.set_title('Percentage of First-Year Enrolments by Ethnicity Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')
    ax.legend(title='Ethnicity', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()


load_and_plot_ucas_data(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\ucas_ungrad.csv")
