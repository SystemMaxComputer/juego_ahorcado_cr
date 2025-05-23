from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Modelo para la tabla 'palabra'
class Palabra(Base):
    __tablename__ = 'palabra'

    id = Column(Integer, primary_key=True)
    contenido = Column(String(20), unique=True, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    dificultad_id = Column(Integer, ForeignKey('dificultad.id'))


# Modelo para la tabla 'dificultad'
class Dificultad(Base):
    __tablename__ = 'dificultad'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)

    # Relación con la tabla 'palabra'
    palabras = relationship('Palabra', backref='dificultad')


# Modelo para la tabla 'categoria'
class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)

    # Relación con la tabla 'palabra'
    palabras = relationship('Palabra', backref='categoria')
