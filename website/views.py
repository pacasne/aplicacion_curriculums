from flask import Blueprint, render_template#las views que no necesiten un login del usuario.
views = Blueprint("views",__name__)

@views.route("/",methods = ["POST","GET"])
def home():
    return render_template("home.html")