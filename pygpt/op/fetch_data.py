import pandas as pd

def load_movie_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    movie_data_path = '/Users/zu/workspaces/ai-cookbook/data/csv/IMDB-Movie-Data.csv'
    movie_data = load_movie_data(movie_data_path)
    print(movie_data.head())