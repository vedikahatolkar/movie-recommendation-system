from flask import request, session, redirect
from database.models import Rating
from database.db import db

# IMPORTANT: import app
from app.app import app


@app.route("/rate", methods=["POST"])
def rate_movie():

    print("RATE ROUTE HIT")  # DEBUG LINE

    user_id = session.get("user_id")

    if not user_id:
        print("NO USER → redirecting to home")
        return redirect("/")   # this is why you go home

    movie = request.form.get("movie")
    rating = int(request.form.get("rating"))

    new_rating = Rating(
        user_id=user_id,
        movie_title=movie,
        rating=rating
    )

    db.session.add(new_rating)
    db.session.commit()

    print("RATING SAVED → redirecting to /recommend")

    return redirect("/recommend?success=1")