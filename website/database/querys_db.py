from .. import db
from ..models import Empleados_Trabajos, Usuarios, Empleados, Trabajos, Clientes, Tipologias, Tematicas
from werkzeug.security import generate_password_hash

def insert_usuarios(password, email, admin):    #accion_tabla
    """def 
                Insertar nuevo usuario en la tabla usuarios
            INPUT
                
                PASSWORD --> STRING\n
                EMAIL --> STRING\n
                ADMIN --> BOOL\n
                
            OUTPUT
                TRUE --> SUCCESFULL\n
                FALSE --> SOMETHING GO WRONG
    """
    try:
        if admin is not None:
            admin = True
        else:
            admin = False

        nuevo_usuario = Usuarios( email = email, password = generate_password_hash(password, method='sha256'), admin = admin)
        db.session.add(nuevo_usuario)
        db.session.commit()
        #insertamos en la tabla con la estructura de con los parámetros

        return True
    except:

        return False