import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# data paths
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed")

# model storage
MODEL_PATH = os.path.join(BASE_DIR, "models")

# TMDB API
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"