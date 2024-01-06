from test_ucas_linegraph import load_data, create_line_graph
import matplotlib.pyplot as plt

def main():
    # Load dataset
    df = load_data()

    # Create a line graph
    create_line_graph(df)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()