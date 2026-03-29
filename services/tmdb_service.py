import requests
from config.config import TMDB_API_KEY, TMDB_BASE_URL, TMDB_IMAGE_URL


# 🔹 Clean Movie Title (VERY IMPORTANT)
def clean_title(title):

    # remove year (1995)
    title = title.split("(")[0]

    # remove alias (a.k.a.)
    if "a.k.a." in title:
        title = title.split("a.k.a.")[0]

    return title.strip()


def get_movie_details(title):

    query = clean_title(title)

    print("🔍 Searching TMDb for:", query)

    url = f"{TMDB_BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }

    response = requests.get(url, params=params).json()

    # ❗ Handle empty results safely
    if not response.get("results"):
        print("❌ No TMDb result for:", query)
        return None

    movie = response["results"][0]

    # Poster
    poster = None
    if movie.get("poster_path"):
        poster = TMDB_IMAGE_URL + movie["poster_path"]

    overview = movie.get("overview", "")
    movie_id = movie.get("id")

    trailer = get_movie_trailer(movie_id) if movie_id else None

    return {
        "poster": poster,
        "overview": overview,
        "trailer": trailer
    }


def get_movie_trailer(movie_id):

    url = f"{TMDB_BASE_URL}/movie/{movie_id}/videos"

    params = {
        "api_key": TMDB_API_KEY
    }

    response = requests.get(url, params=params).json()

    for video in response.get("results", []):
        if video.get("type") == "Trailer":
            return f"https://www.youtube.com/watch?v={video['key']}"

    return None