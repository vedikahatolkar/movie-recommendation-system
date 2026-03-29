import pandas as pd
import os
from config.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def preprocess():

    movies = pd.read_csv(os.path.join(RAW_DATA_PATH, "movies.csv"))
    ratings = pd.read_csv(os.path.join(RAW_DATA_PATH, "ratings.csv"))

    merged = pd.merge(ratings, movies, on="movieId")

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    merged.to_csv(os.path.join(PROCESSED_DATA_PATH, "merged_data.csv"), index=False)

    matrix = merged.pivot_table(
        index="userId",
        columns="title",
        values="rating"
    ).fillna(0)

    matrix.to_csv(os.path.join(PROCESSED_DATA_PATH, "user_movie_matrix.csv"))

    return matrix