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

# Ruta usuarios 
# /home/nahomi/Downloads/Proyecto-Final-B1/trabjo-final-1bim-grupo-007/DATA/usuarios_red_x.csv
usuarios_csv = pd.read_csv("DATA/usuarios_red_x.csv")

# print(usuarios_csv.usuario)

# Ingresar datos usuario
'''
for u in usuarios_csv.usuario:
        usuario = Usuario(
                usuarioNombre = u
                )

        session.add(usuario)
        print(usuario)
'''

# Ingresar datos publicacion

# Ruta publicaciones 
# /home/nahomi/Downloads/Proyecto-Final-B1/trabjo-final-1bim-grupo-007/DATA/usuarios_publicaciones.csv
publicaciones_csv = pd.read_csv("DATA/usuarios_publicaciones.csv", delimiter='|')

print(publicaciones_csv)

session.commit()