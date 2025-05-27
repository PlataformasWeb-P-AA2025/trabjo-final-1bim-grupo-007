# Crear 5 consultas adicionales

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_data import Usuario, Publicacion, Reaccion

import pandas as pd

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Usuarios que reaccionaron a sus propias publicaciones

usuarios_egocentricos = session.query(Usuario).join(Publicacion).\
						join(Reaccion).filter(
							Reaccion.usuario_id.like(Publicacion.usuario_id)
						).all()

for u in usuarios_egocentricos:
	print(u)

# Emociones mas comunes por usuario


# Usuarios sin publicaciones pero con reacciones


# Publicaciones con mas reacciones


# Usuarios sin ninguna reaccion ni publicacion