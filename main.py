from src.data_preprocessing import preprocess
from src.similarity_engine import compute_similarity

print("Loading and preprocessing dataset...")

matrix = preprocess()

print("Computing similarity matrix...")

compute_similarity(matrix)

print("Model ready!")