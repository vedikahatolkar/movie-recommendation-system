from flask import Blueprint, request, redirect
from database.models import Watchlist
from database.db import db

user_bp = Blueprint("user", __name__)

@user_bp.route("/watchlist/add", methods=["POST"])
def add_watchlist():

    movie = request.form["movie"]

    item = Watchlist(user_id=1, movie_title=movie)

    db.session.add(item)

    db.session.commit()

    return redirect("/watchlist")