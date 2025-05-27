# Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" 
# que sean de usuarios que cuyos nombre no inicien con vocal.

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

# Uso de in_() para evitar un like() || ...
# El uso de and_ permite comparar cada volcal, no se como explicarlo
# ~ eso es para negar una expresion
# ilike() es insensible a mayusculas o minusculas
reacciones = session.query(Reaccion, Usuario).join(Usuario).\
			filter(Reaccion.tipo_emocion.in_(["alegre", "enojado", "pensativo"])).\
			filter(
				and_(
					~Usuario.usuarioNombre.ilike('a%'),
					~Usuario.usuarioNombre.ilike('e%'),
					~Usuario.usuarioNombre.ilike('i%'),
					~Usuario.usuarioNombre.ilike('o%'),
					~Usuario.usuarioNombre.ilike('u%')
				)		
			).all()

print("Listar todas las reacciones de tipo alegre, enojado, pensativo")

for r in reacciones:
	print(f"Usuario {r.Usuario.usuarioNombre} y su reaccion {r.Reaccion.tipo_emocion}")