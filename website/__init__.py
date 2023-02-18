from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from datetime import timedelta


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1111"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 5)
    db.init_app(app) #inicializando

    from .views import views
    app.register_blueprint(views,url_prefix = "/")
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)
     #copias que se ponen por encima de app. Esto se va cargando por encima de app que es como la base. app es el marco, director de orquesta.
    from .models import Empleados
    @login_manager.user_loader
    def load_user(id):
        return Empleados.query.get(int(id))
    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Create database")

