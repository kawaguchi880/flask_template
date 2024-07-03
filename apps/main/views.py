from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # ログイン処理
        session["user"] = {"username": "test"}
        return redirect(url_for("main.index"))
    return render_template("main/login.html")
