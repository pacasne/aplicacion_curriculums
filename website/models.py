from . import db
from flask_login import UserMixin #tabla del usuario
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

Empleados_Trabajos = db.Table('Empleados_trabajos',Base.metadata,
    db.Column('ID_Empleados', db.Integer, db.ForeignKey('Empleados.ID')),
    db.Column('ID_Trabajos', db.Integer, db.ForeignKey('Trabajos.ID'))
)#esta es la tabla intermedia

class Empleados(db.Model,UserMixin,Base):#db.Model es un método que indica que es una tabla
    ID = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(150))#entre paréntesis va el número de carácteres máximos
    apellido1 = db.Column(db.String(150))
    apellido2 = db.Column(db.String(150))
    DNI = db.Column(db.String(20))
    teléfono = db.Column(db.String(30))
    direccion = db.Column(db.String(150))
    ciudad = db.Column(db.String(100))
    email = db.Column(db.String(150))
    admin = db.Column(db.Boolean)
    trabajos = db.relationship("Trabajos",secondary = Empleados_Trabajos, back_populate = "empleados")# esta columna la creamos para apuntar a la tabla intermedia.
    

class Trabajos(db.Model,Base):
    ID = db.Column(db.Integer,primary_key = True)
    nombre_trabajo = db.Column(db.String(400))
    localizacion = db.Column(db.String(150))
    ID_tipologia = db.Column(db.Integer)
    ID_tematica = db.Column(db.Integer)
    ID_cliente = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime(timezone = True),default = func.now())#para que no pete que ponga la actual
    fecha_final =  db.Column(db.DateTime(timezone = True),default = func.now())
    empleados = db.relationship("Empleados",secondary = Empleados_Trabajos, back_populate = "trabajos")
