from flask import Blueprint, render_template, request#las views que no necesiten un login del usuario.
views = Blueprint("views",__name__)

@views.route("/",methods = ["POST","GET"])
def home():
    return render_template("home.html")

@views.route("/signup",methods = ["POST","GET"])#esto es lo que hace que muestre a url
def signup():
    return render_template("signup.html")