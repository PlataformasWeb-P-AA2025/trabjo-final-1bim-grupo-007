from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_data import Usuario, Publicacion, Reaccion

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

import pandas as pd

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = 'Molly' #nombre del usuario del que se desea saber el numero de publicaciones

#se hace una consulta para saber si el usuario existe en la base de datos
usuario = session.query(Usuario).filter_by(usuarioNombre=nombre_usuario).first()

#print(usuario)
if usuario:
    print(f"Publicaciones de {usuario.usuarioNombre}:")
    if usuario.publicaciones:
        for i in usuario.publicaciones:
            print(f"- {i.publicacion}")
    else:
        print("Usuario no tiene publicaciones hasta el momento")
else:
    print("Usuario no existe")
