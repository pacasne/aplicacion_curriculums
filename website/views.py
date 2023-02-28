from flask import Blueprint, render_template, request#las views que no necesiten un login del usuario.
from .database import querys_db as qdb


views = Blueprint("views",__name__)

@views.route("/",methods = ["POST","GET"])
def home():
    return render_template("home.html")

@views.route("/signup",methods = ["POST","GET"])#esto es lo que hace que muestre a url(POST manda ordenes del front al servidor)
def signup():
    #request.form.get('email1')#la clase request es lo que nos permite interactuar con la interactuar con la información recogida del html(interactuar con el html)
    if request.method == "POST":
        email1 = request.form.get("email1")
        email2 = request.form.get("email2")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        administrador = request.form.get("administrador")

        if email1 == email2 and password1 == password2:
            resultado = qdb.insert_usuarios(password1, email1,administrador)    
            return render_template("signup.html",resultado = resultado)

    return render_template("signup.html")


@views.route("/login",methods = ["POST","GET"])#esto es lo que hace que muestre a url
def login():
    return render_template("login.html")