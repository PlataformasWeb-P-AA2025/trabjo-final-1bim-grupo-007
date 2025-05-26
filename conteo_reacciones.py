# Obtener un reporte de reacciones en función del número de 
# veces que fueron usadas

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

# Obtener todos los registros de 
# la entidad Reaccion
# Hay dos formas, usando SQLAlchemy o usando pandas

# SQLAlchemy: solo imprimir datos, y no se necesita manipular los datos
resultadosSQL = session.query(
							# Defino el atributo que quiero recuperar
							Reaccion.tipo_emocion,
							# Usa la funcion de agregacion count() de SQL.
							# para contar las veces en las que aparece cada 
							# tipo de emocion 
							func.count(Reaccion.tipo_emocion).label('conteo')
						).group_by(Reaccion.tipo_emocion).order_by(func.count(Reaccion.tipo_emocion).desc()).all()

# Pandas: usar en caso de que se quieran hacer graficas, reportes, etc.
# Se traen los datos de la BD
resultadosPandas = session.query(Reaccion.tipo_emocion).all()
# Se convierte la lista de tuplas en una lista plana
emociones = [r[0] for r in resultadosPandas]
# Crea el dataframe y agrupa
df = pd.DataFrame({'emocion': emociones})
conteo = df['emocion'].value_counts()

print("---------------------------------------")
print("Reporte de emociones usando sqlalchemy:")
for emocion, cantidad in resultadosSQL:
	print(f"{emocion}: {cantidad} veces")

print("---------------------------------------")
print("Reporte de emociones usando Pandas:")
print(conteo)