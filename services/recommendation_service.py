from src.recommendation_model import Recommender
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

#  NEW (for personalization)
from database.models import Rating


# Load collaborative model
recommender = Recommender()

def recommend(movie_name):
    return recommender.recommend(movie_name)


# Load content-based data
movies_df = pd.read_csv("data/processed/merged_data.csv")

movies_df["content"] = movies_df["genres"].fillna('') + " " + movies_df["title"]

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df["content"])

def get_content_recommendations(movie_title, top_n=10):

    if movie_title not in movies_df["title"].values:
        return []

    idx = movies_df[movies_df["title"] == movie_title].index[0]

    # Compute similarity ONLY for this movie
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    sim_indices = sim_scores.argsort()[::-1][1:top_n+1]

    return movies_df.iloc[sim_indices]["title"].tolist()



# Hybrid Recommendation
def hybrid_recommend(movie_title, top_n=10):

    collab_results = recommend(movie_title)

    content_results = get_content_recommendations(movie_title, top_n)

    final = list(dict.fromkeys(collab_results + content_results))[:top_n]

    return final


#  NEW: Personalized Recommendation

def recommend_for_user(user_id, top_n=10):

    # Get user ratings
    user_ratings = Rating.query.filter_by(user_id=user_id).all()

    # Cold start (no ratings yet)
    if not user_ratings:
        return hybrid_recommend("Toy Story (1995)", top_n)

    # Pick highest rated movie
    fav_movie = max(user_ratings, key=lambda x: x.rating).movie_title

    # Use hybrid recommendation
    return hybrid_recommend(fav_movie, top_n)