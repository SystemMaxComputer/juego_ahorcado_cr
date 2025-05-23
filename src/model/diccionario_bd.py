import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.db import Palabra, Dificultad, Categoria
from src.model.i_diccionario import IDiccionario


class DiccionarioBD(IDiccionario):
    """
        Representa un diccionario de palabras que pueden ser utilizadas en un juego de adivinanza.

        Attributes:
            palabras (list[str]): Lista de palabras cargadas desde un archivo de texto.
    """

    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """

        # Configurar la conexión a PostgreSQL
        url_conexion = "postgresql://gthomas:@localhost:5432/ahorcado"

        # Crear el motor de conexión
        engine = create_engine(url_conexion, echo=True)

        # Crear la sesión para interactuar con la base de datos
        session = sessionmaker(bind=engine)
        self.data_base_session = session()

    def obtener_palabra(self, categoria: str, dificultad: str) -> str:
        """
            Obtiene una palabra aleatoria del diccionario.

            Returns:
                str: Una palabra seleccionada aleatoriamente de la lista de palabras cargadas.
        """
        palabras_seleccioandas = self.data_base_session.query(Palabra).join(Dificultad).join(Categoria).filter(
            Dificultad.nombre == dificultad, Categoria.nombre == categoria).all()

        indice_aleatorio = random.randint(0, len(palabras_seleccioandas) - 1)

        return palabras_seleccioandas[indice_aleatorio].contenido
