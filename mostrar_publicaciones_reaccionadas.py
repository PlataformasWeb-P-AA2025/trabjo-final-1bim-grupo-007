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
    print(f"Publicaciones en las que reacciono {usuario.usuarioNombre}:")
    # Iteramos solo sobre las reacciones del usuario
    if usuario.reacciones:
        for reaccion in usuario.reacciones:
            pub = reaccion.publicacion  # Relación Publicacion
            print(f"- Publicacion ID {pub.id} con contenido: '{pub.publicacion[:50]}...'")
            print(f"  Tipo de reacción: {reaccion.tipo_emocion}")
            if reaccion.comentario:
                print(f"  Comentario: {reaccion.comentario}")
    else:
        print("Este usuario no ha reaccionado a ninguna publicacion")
else:
    print("Usuario no encontrado.")