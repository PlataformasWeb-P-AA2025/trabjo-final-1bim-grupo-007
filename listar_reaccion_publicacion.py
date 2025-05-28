from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

if usuario:
    print(f"Reacciones a las publicaciones de {usuario.usuarioNombre}:")
    
    if usuario.publicaciones:
        for publicacion in usuario.publicaciones:
            print(f"\nPublicacion: {publicacion.publicacion}")
            if publicacion.reacciones:
                for reaccion in publicacion.reacciones:
                    print(f" - Emocion: {reaccion.tipo_emocion}")
            else:
                print("  No tiene reacciones")
    else:
        print("El usuario no tiene publicaciones.")
else:
    print("Usuario no encontrado.")