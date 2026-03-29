import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os
from config.config import MODEL_PATH
from src.utils import save_pickle

def compute_similarity(matrix):

    similarity = cosine_similarity(matrix.T)

    similarity_df = pd.DataFrame(
        similarity,
        index=matrix.columns,
        columns=matrix.columns
    )

    os.makedirs(MODEL_PATH, exist_ok=True)

    save_pickle(similarity_df, os.path.join(MODEL_PATH, "similarity_matrix.pkl"))

    return similarity_df