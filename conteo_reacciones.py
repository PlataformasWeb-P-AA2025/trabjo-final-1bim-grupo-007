# Obtener un reporte de reacciones en función del número de 
# veces que fueron usadas

from sqlalchemy import create_engine
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
reacciones = session.query(Reaccion).all()

r_tipo_emocion = []

for r in reacciones:
	# print(r.tipo_emocion)
	r_tipo_emocion.append(r.tipo_emocion) 

# print(r_tipo_emocion)

df_tipo_reaccion = pd.DataFrame({'emocion': r_tipo_emocion})

tipo_reaccion_conteo = len(df_tipo_reaccion['emocion'].unique())	

print(tipo_reaccion_conteo)