import pandas as pd
import matplotlib.pyplot as plt

def load_ucas_linegraph(csv_path):
    # Load dataset
    df = pd.read_csv(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_ungrad.csv")

    # Filtering the DataFrame to include only relevant columns
    df_plot = df[['Time', 'Ethnicity', 'Percentage']]

    # Use .loc to avoid SettingWithCopyWarning
    df_plot.loc[:, 'Percentage'] = pd.to_numeric(df_plot['Percentage'], errors='coerce')

    # Aggregate data by taking the mean for duplicate entries
    df_pivot = df_plot.groupby(['Time', 'Ethnicity']).mean().unstack()

    # Plotting the line graph
    df_pivot.plot(kind='line', marker='o', figsize=(10, 6))

    # Adding labels and title
    plt.title('Percentage of First Year Enrolments by Ethnicity (2016 - 2020)')
    plt.xlabel('Academic Year')
    plt.ylabel('Percentage')
    plt.grid(True)
    plt.legend(title='Ethnicity', bbox_to_anchor=(1, 1))

    # Show the plot
    plt.show()

if __name__ == "__main__":
    load_ucas_linegraph(r"path/to/ucas_ungrad.csv")
