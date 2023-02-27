from . import db
from flask_login import UserMixin #tabla del usuario
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
#empleado1.trabajos.append(trabajo1)
#trabajo1.empleados.append(empleados1)
Empleados_Trabajos = db.Table('Empleados_trabajos',Base.metadata,
    db.Column('id_Empleados', db.Integer, db.ForeignKey('Empleados.id')),
    db.Column('id_Trabajos', db.Integer, db.ForeignKey('Trabajos.id'))
)#esta es la tabla intermedia

class Usuarios(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    admin = db.Column(db.Boolean)    

class Empleados(db.Model,Base):#db.Model es un método que indica que es una tabla
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(150))#entre paréntesis va el número de carácteres máximos
    apellido1 = db.Column(db.String(150))
    apellido2 = db.Column(db.String(150))
    DNI = db.Column(db.String(20))
    teléfono = db.Column(db.String(30))
    direccion = db.Column(db.String(150))
    ciudad = db.Column(db.String(100))
    email = db.Column(db.String(150))
    trabajos = db.relationship("Trabajos",secondary = Empleados_Trabajos, back_populates = "empleados")# esta columna la creamos para apuntar a la tabla intermedia.
    

class Trabajos(db.Model,Base):
    id = db.Column(db.Integer,primary_key = True)
    nombre_trabajo = db.Column(db.String(400))
    localizacion = db.Column(db.String(150))
    id_tipologia = db.Column(db.Integer, db.ForeignKey('Tipologias.id'))
    id_tematica = db.Column(db.Integer, db.ForeignKey('Tematicas.id'))
    id_cliente = db.Column(db.Integer, db.ForeignKey('Clientes.id'))
    fecha_inicio = db.Column(db.DateTime(timezone = True),default = func.now())#para que no pete que ponga la actual
    fecha_final =  db.Column(db.DateTime(timezone = True),default = func.now())
    empleados = db.relationship("Empleados",secondary = Empleados_Trabajos, back_populates = "trabajos")
    

class Clientes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_corto = db.Column(db.String(150))
    nombre_empresa = db.Column(db.String(200))
    NIF = db.Column(db.String(150))
    direccion = db.Column(db.String(250))
    trabajos = db.relationship('Trabajos')

class Tipologias(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    abreviatura_tipologia = db.Column(db.String(20))
    nombre_tipologia = db.Column(db.String(150))
    trabajos = db.relationship('Trabajos')

class Tematicas(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    abreviatura_tematica = db.Column(db.String(50))
    nombre_tematica = db.Column(db.String(150))
    trabajos = db.relationship('Trabajos')
                            