import pandas as pd
import matplotlib.pyplot as plt

def load_ucas_bargraph():
    """
    Generates a grouped bar chart comparing UCAS applications by ethnic group for June deadlines in 2019 and 2020.

    The function reads a dataset from an Excel file, filters it for June deadline applications in 2019 and 2020,
    excludes entries for 'Men' and 'Women', converts relevant columns to appropriate data types using .loc,
    pivots the DataFrame, and plots a grouped bar chart using Matplotlib.

    Parameters:
    None

    Returns:
    None
        The function generates a plot using Matplotlib to visually represent the comparison of UCAS applications.
    """
    # Load dataset
    ucas_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\ucas_data.xlsx")

    # Filter data for June deadline applications in 2019 and 2020, excluding 'Men' and 'Women'
    june_deadlines_data = ucas_data[
        (ucas_data['Entry of Application'] == 'June deadline applications') & 
        (ucas_data['Year'].isin([2019, 2020])) & 
        (~ucas_data['Ethnic Group'].isin(['Men', 'Women']))
    ]

    # Convert 'Number of Applications' to numeric, handling non-numeric values
    june_deadlines_data.loc[:, 'Number of Applications'] = pd.to_numeric(june_deadlines_data['Number of Applications'], errors='coerce').fillna(0)

    # Convert 'Ethnic Group' to categorical
    june_deadlines_data.loc[:, 'Ethnic Group'] = pd.Categorical(june_deadlines_data['Ethnic Group'])

    # Pivot the DataFrame for easy plotting
    pivot_data = june_deadlines_data.pivot(index='Ethnic Group', columns='Year', values='Number of Applications').reset_index()

    # Plotting the grouped bar chart
    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    x_values = range(len(pivot_data))

    plt.bar(x_values, pivot_data[2019], width=bar_width, label='2019', color='green')
    plt.bar([x + bar_width for x in x_values], pivot_data[2020], width=bar_width, label='2020', color='pink')

    # Customising the plot labels and title
    plt.xlabel('Ethnic Group')
    plt.ylabel('Number of Applications')
    plt.title('Comparison of UCAS Applications by Ethnic Group (June Deadlines, 2019-2020)')
    plt.xticks([x + bar_width / 2 for x in x_values], pivot_data['Ethnic Group'])  # Adjust x-axis tick positions
    plt.legend(title='Year')

    plt.show()

if __name__ == "__main__":
    load_ucas_bargraph()
