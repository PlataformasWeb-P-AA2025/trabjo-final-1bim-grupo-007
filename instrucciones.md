// Por si las dudas se debe eliminar y recrear el contenedor con la base ya creada.

docker rm -f postgres-db

// Inicia el servicio Docker.

sudo systemctl start docker

// Verificar que esté activo.

sudo systemctl status docker

// Correr el contenedor.

docker run --name postgres-db \
  -e POSTGRES_USER=richard \
  -e POSTGRES_PASSWORD=123 \
  -e POSTGRES_DB=richitoyhumita \
  -p 5432:5432 \
  -d postgres

//Si se desea pausar y remover el antiguo contenedor se usa:

//Para detenerlo
docker stop postgres-db 

//Para removerlo
docker rm postgres-db

// Si quiere conserva el viejo contenedor y usar uno distinto se usa otro nombre.

docker run --name postgres-db-richard \
  -e POSTGRES_USER=richard \
  -e POSTGRES_PASSWORD=123 \
  -e POSTGRES_DB=richitoyhumita \
  -p 5433:5432 \
  -d postgres
    
// Asegurarse de que el contenedor está corriendo.

docker ps

//Instalar el driver de PostgreSQL en tu entorno Python en caso de no tenerlo.

pip install psycopg2-binary

// Permitir usar el Docker sin sudo.

sudo usermod -aG docker $USER

// Inicializar Docker.

docker start postgres-db

// Comando para abrir la base de datos por defecto del docker de postgres 

docker exec -it postgres-db psql -U nahomi -d postgres

// Comando para crear la base de datos

CREATE DATABASE richitoyhumita;

// En caso de tener la base de datos creada se va directamente a este usuario

docker exec -it postgres-db psql -U nahomi -d richitoyhumita

// Para salir de la interfaz de 

\q

