# Importing all necessary  Python data visualisation and analysis libraries
import pandas as pd
import matplotlib.pyplot as plt

def load_ucas_linegraph(csv_path):
    """
    Load data from a CSV file and create a line graph.

    Parameters:
    - csv_path (str): The file path to the CSV containing the data.

    Returns:
    None
    """
    # Load dataset from the specified CSV file path
    df = pd.read_csv(csv_path)

    # Filter the DataFrame to include only relevant columns
    df_plot = df[['Time', 'Ethnicity', 'Percentage']]

    # Use .loc to avoid SettingWithCopyWarning by explicitly referencing the DataFrame
    df_plot.loc[:, 'Percentage'] = pd.to_numeric(df_plot['Percentage'], errors='coerce')

    # Aggregate data by taking the mean for duplicate entries
    df_pivot = df_plot.groupby(['Time', 'Ethnicity']).mean().unstack()

    # Plotting the line graph
    df_pivot.plot(kind='line', marker='o', figsize=(10, 6))

    # Adding labels and title to the plot
    plt.title('Percentage of First Year Enrolments by Ethnicity (2016 - 2020)')
    plt.xlabel('Academic Year')
    plt.ylabel('Percentage')
    plt.grid(True)
    
    # Display legend with title on the right side of the plot
    plt.legend(title='Ethnicity', bbox_to_anchor=(1, 1))

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Execute the function with the path to the CSV file
    load_ucas_linegraph(r"path/to/ucas_ungrad.csv")
