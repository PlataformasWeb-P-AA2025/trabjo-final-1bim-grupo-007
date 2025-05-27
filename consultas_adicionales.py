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

# Se unen las tablas Usuario, Publicacion y Reaccion
# el filter comprueba que el usuario_id de la reaccion sea igual al id
# del usuario que hizo la publicacion

'''
usuarios_egocentricos = session.query(Usuario).\
						join(Publicacion).\
						join(Reaccion).\
						filter(Reaccion.usuario_id == Usuario.id).\
						order_by(Reaccion.usuario_id).all()

for u in usuarios_egocentricos:
	print(u)
'''

# Emociones mas comunes por usuario
# Primero defino lo que quiero recuperar, el nombre del usuario,
# el tipo de emocion, y el conteo de esta emocion.
# Con ayuda de func, cuento por usuario cada reaccion que tuvo.
# Para que se entienda mejor, agrupo primero los estudiantes y sus reacciones
# y luego dentro de esta agrupacion, cuento las veces que uso cada emocion

'''
emociones_usuarios = session.query(Usuario.usuarioNombre, 
									Reaccion.tipo_emocion,
									func.count(Reaccion.tipo_emocion).label('conteo')).\
						join(Reaccion).\
						group_by(Usuario.id, Reaccion.tipo_emocion).\
						order_by(Usuario.usuarioNombre, func.count(Reaccion.tipo_emocion).desc()).all()

for u in emociones_usuarios:
	print(u)
'''

# Usuarios sin publicaciones pero con reacciones
# Primero especifico que solo quiero el usuario
# luego el outerjoin me ayuda a unir con publicaciones
# asi no existan. Despues se ve que el usuario tenga al menos 
# una reaccion con ayuda del join. Finalmente se filtran 
# a los que no tienen publicacion

'''
usuarios_reaccionadores = session.query(Usuario).\
						outerjoin(Publicacion).\
						join(Reaccion).\
						filter(Publicacion.id == None).all()
for u in usuarios_reaccionadores:
	print(u)
'''

# Publicaciones con mas reacciones
# Especifico que solo quiero la Publicacion junto a el numero de reacciones
# el outer me ayuda a tener en cuenta hasta aquellas publicaciones sin
# reacciones. Se cuentan las reacciones de cada publicacion, se agrupan y se ordenan

'''
publicaciones_top = session.query(
								Publicacion,
								func.count(Reaccion.id).label("num_reacciones")
							).outerjoin(Reaccion).\
							group_by(Publicacion.id).\
							order_by(func.count(Reaccion.id).desc()).all()

for u in publicaciones_top:
	print(f"Publicacion hecha por {u.Publicacion.usuario.usuarioNombre}, tiene {u.num_reacciones} reaccion/es")
'''

# Usuarios sin ninguna reaccion ni publicacion
# Como en los anteriores, hago un outerjoin para considerar aquellos que no estan
# en la tabla, y luego filtro sus id
usuarios_fantasmas = session.query(Usuario).\
						outerjoin(Publicacion).\
						outerjoin(Reaccion).\
						filter(
							and_(
									Publicacion.id == None, 
									Reaccion.id == None
								)
						).all()

i= 1
for u in usuarios_fantasmas:
	print(f"{i} El usuario {u.usuarioNombre} no tiene ninguna publicacion o reaccion")
	i = i + 1