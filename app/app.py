from flask import Flask, render_template, request, session, redirect
import pandas as pd
import os

from config.config import PROCESSED_DATA_PATH
from app.recommendation_api import get_recommendations
from services.recommendation_service import recommend_for_user
from database.db import db

# ✅ CREATE APP FIRST
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "supersecretkey"

# ✅ DATABASE CONFIG (AFTER app creation)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ✅ REGISTER BLUEPRINT
from app.auth_routes import auth
app.register_blueprint(auth)

# ✅ LOAD DATA
matrix = pd.read_csv(
    os.path.join(PROCESSED_DATA_PATH, "user_movie_matrix.csv"),
    index_col=0
)

movies = list(matrix.columns)

# ================= ROUTES =================

@app.route("/")
def index():
    return render_template("index.html", movies=movies)


@app.route("/recommend", methods=["GET", "POST"])
def recommend():

    if request.method == "GET":
        return redirect("/")

    user_id = session.get("user_id")

    from app.recommendation_api import get_recommendations, get_user_recommendations

    if user_id:
        recommendations = get_user_recommendations(user_id)
    else:
        movie = request.form["movie"]
        recommendations = get_recommendations(movie)

    return render_template(
        "results.html",
        recommendations=recommendations
    )


# ✅ IMPORT OTHER ROUTES
from app.movie_routes import *

# ✅ CREATE TABLES
with app.app_context():
    db.create_all()

# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)