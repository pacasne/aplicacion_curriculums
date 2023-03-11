from flask import Blueprint, render_template, request, flash, session#las views que no necesiten un login del usuario.
from flask_login import login_user, login_required, logout_user, current_user
from .database import querys_db as qdb
from .models import Usuarios
from werkzeug.security import check_password_hash

views = Blueprint("views",__name__)

@views.route("/",methods = ["POST","GET"])
def home():
    return render_template("home.html",User_register = current_user)

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
            user = qdb.insert_usuarios(password1, email1,administrador)
            if user is not None and user is not False:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                session.permanent = True    
                return render_template("signup.html",resultado = True,User_register = current_user)
            else:
                return render_template("signup.html",resultado = False,User_register = current_user)

    return render_template("signup.html",User_register = current_user)


@views.route("/login",methods = ["POST","GET"])#esto es lo que hace que muestre a url
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Usuarios.query.filter_by(email=email).first()
        if not current_user.is_active:
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    session.permanent = True
    return render_template("login.html",User_register = current_user)

@views.route('/modification', methods = ["POST","GET"])
@login_required
def modification():
    return render_template("modification.html",User_register = current_user)
