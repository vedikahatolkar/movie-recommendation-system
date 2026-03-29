from flask import Blueprint, render_template, request, redirect, session
from database.models import User
from database.db import db

auth = Blueprint("auth", __name__)

# SIGNUP
@auth.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        # ✅ DIRECT LOGIN AFTER SIGNUP
        session["user_id"] = user.id

        return redirect("/")   # ✅ GO HOME (NOT LOGIN)

    return render_template("signup.html")


# LOGIN
@auth.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user_id"] = user.id
            return redirect("/")   # ✅ GO HOME

    return render_template("login.html")


# LOGOUT
@auth.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/")