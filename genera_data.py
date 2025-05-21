from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos 

engine = create_engine(cadena_base_datos)
	
Base = declarative_base()

class Usuario(Base):
	__tablename__ = 'usuario'
	id = Column(Integer, primary_key=True)
	usuarioNombre = Column(String(50), nullable=False)

	publiciones =relationship("Publicacion", back_populates ="usuario")
	reacciones = relationship("Reaccion", back_populates = "usuario")

	def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}')"

class Publicacion(Base):
	__tablename__ = 'publicacion'
	id = Column(Integer, primary_key=True)
	publicacion = Column(String)
	usuario_id = Column(Integer, ForeignKey('usuario_id'),nullable = False)

	usuario = relationship('Usuario', back_populates='publicaciones')
    reacciones = relationship('Reaccion', back_populates='publicacion')

    def __repr__(self):
        return f"Publicacion(id={self.id}, autor='{self.usuario.nombre}', contenido='{self.contenido[:30]}...')"


class Reaccion(Base):
    __tablename__ = 'reaccion'
    id = Column(Integer, primary_key=True)
    tipo_emocion = Column(String(20), nullable=False)

    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='reacciones')
    publicacion = relationship('Publicacion', back_populates='reacciones')

    __table_args__ = (
        UniqueConstraint('usuario_id', 'publicacion_id', name='uix_usuario_publicacion'),
    )

    def __repr__(self):
        return(
            f"Reaccion(id={self.id}, usuario='{self.usuario.nombre}', "
            f"publicacion_id={self.publicacion_id}, tipo_emocion='{self.tipo_emocion}')"
        )

Base.metadata.create_all(engine)