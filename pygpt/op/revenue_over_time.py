import pandas as pd
import matplotlib.pyplot as plt


def load_movie_data(file_path):
    return pd.read_csv(file_path)


def plot_revenue_over_time(movie_data):
    # Group by year and sum up revenue
    revenue_per_year = movie_data.groupby('Year')['Revenue_Millions'].sum()

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(revenue_per_year.index, revenue_per_year.values)
    plt.title('Total Movie Revenue over Time')
    plt.xlabel('Year')
    plt.ylabel('Total Revenue (Millions)')
    plt.show()

    return plt

if __name__ == "__main__":
    movie_data_path = '/Users/zu/workspaces/ai-cookbook/data/csv/IMDB-Movie-Data.csv'
    movie_data = load_movie_data(movie_data_path)
    plot_revenue_over_time(movie_data)