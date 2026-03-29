from src.utils import load_pickle
from config.config import MODEL_PATH
import os

class Recommender:

    def __init__(self):

        path = os.path.join(MODEL_PATH, "similarity_matrix.pkl")
        self.similarity_df = load_pickle(path)

    def recommend(self, movie, n=5):

        if movie not in self.similarity_df.columns:
            return []

        sim = self.similarity_df[movie].sort_values(ascending=False)

        return list(sim.iloc[1:n+1].index)