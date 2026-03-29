from services.recommendation_service import hybrid_recommend, recommend_for_user
from services.tmdb_service import get_movie_details


def get_recommendations(movie):

    recs = hybrid_recommend(movie)

    results = []

    for m in recs:
        details = get_movie_details(m)

        if details:
            results.append({
                "title": m,
                "poster": details["poster"]
            })

    return results


# ✅ IMPORTANT: FOR LOGGED-IN USER
def get_user_recommendations(user_id):

    recs = recommend_for_user(user_id)

    results = []

    for m in recs:
        details = get_movie_details(m)

        if details:
            results.append({
                "title": m,
                "poster": details["poster"]
            })

    return results