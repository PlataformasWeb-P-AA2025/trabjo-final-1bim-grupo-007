// Inicializar Docker

docker start postgres-db

// Comando para abrir la base de datos por defecto del docker de postgres 

docker exec -it postgres-db psql -U nahomi -d postgres

// Comando para crear la base de datos

CREATE DATABASE richitoyhumita;

// En caso de tener la base de datos creada se va directamente a este usuario

docker exec -it postgres-db psql -U nahomi -d richitoyhumita

// Para salir de la interfaz de 

\q

