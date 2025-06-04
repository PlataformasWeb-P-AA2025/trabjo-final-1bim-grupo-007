# Promts escritos para ChatGPT

# Consulta de reaciones_usuarios.py
## Promt:

Hola.
Estoy tratando de hacer esta consulta:
Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.

A ver, y estaba tratando con la funcion que esta en la imagen

Entonces, me puse a pensar y no se si haya una funcion like not o algo asi, porque no quiero escribir todas las letras del abecedario :c

# Consulta conteo_reacciones.py
## Promt:

Miraaa, ayudame con esta consulta por fis, no se como hacer muy bien, ahi trate de usar algunas cosas, pero creo que me estoy complicando la vida, la consulta esta en el comentario 1 y 2
 Obtener un reporte de reacciones en función del número de 
 veces que fueron usadas

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

 se importa la clase(s) del 
 archivo genera_tablas
from genera_data import Usuario, Publicacion, Reaccion

import pandas as pd

 se importa información del archivo configuracion
from configuracion import cadena_base_datos
 se genera enlace al gestor de base de
 datos
 para el ejemplo se usa la base de datos
 sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

 Obtener todos los registros de 
 la entidad Reaccion
reacciones = session.query(Reaccion).all()

r_tipo_emocion = []

for r in reacciones:
	# print(r.tipo_emocion)
	r_tipo_emocion.append(r.tipo_emocion) 

 print(r_tipo_emocion)

df_tipo_reaccion = pd.DataFrame({'emocion': r_tipo_emocion})

tipo_reaccion_conteo = len(df_tipo_reaccion['emocion'].unique())	

print(tipo_reaccion_conteo)

# Configuracion Docker postgres

## Prompt:

Mira guapo, hace mucho tiempo te estaba pidiendo ayuda con la inserción de reacciones, buscando los objetos ya insertados de Usuario y Publicación, estos datos los leía de un csv, y luego de eso te pedí ayuda en consultas. Verás, y siempre te he pedido que me ayudes con SQLAlchemy, porque eso estabamos usando, pero quiero realizar lo siguiente:

Usar una base de datos Postgres a través de Docker. 

Y pues ahí hacer las consultas que te dije, pero lo que me interesa saber es la instalación, como usarlo, y como generar las consultas que ya tengo en mi git. Porque ya las tengo, pero capaz y debo convertirlas para que me entienda postgrest.

## Prompt:
Como instalo el Docker es que aún no lo tengo :'( no tengo nada de postgrest

## Prompt:
nahomi@Ubuntu22:~/Desktop$ docker run --name postgres-db   -e POSTGRES_USER=nahomi   -e POSTGRES_PASSWORD=nahomi123   -e POSTGRES_DB=mi_base   -p 5432:5432   -d postgres
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Run 'docker run --help' for more information

Me salio este error al tratar de hacer el paso 3 uwu

## Prompt:
yaaaa ya le cambie la configuracion de mi proyecto jeje 

luego de eso que hago? Debo levantar la BD en postgres antes, o que sigue? Estoy emocionadaaaaa uwu

## Prompt:
a ver, debo abrir la terminal, y por ejemplo me ubico en home, y ahi pongo:

docker exec -it postgres-db psql -U nahomi

nahomi@Ubuntu22:~$ docker exec -it postgres-db psql -U nahomi
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "nahomi" does not exist