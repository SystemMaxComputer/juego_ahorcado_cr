import random
from src.model.i_diccionario import IDiccionario


class DiccionarioFile(IDiccionario):
    """
        Representa un diccionario de palabras que pueden ser utilizadas en un juego de adivinanza.

        Attributes:
            palabras (list[str]): Lista de palabras cargadas desde un archivo de texto.
    """

    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
            Carga las palabras desde el archivo "assets/palabras.txt".

            Returns:
                list[str]: Lista de palabras leídas del archivo, eliminando espacios en blanco y saltos de línea.
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self, categoria: str, dificultad: str) -> str:
        """
            Obtiene una palabra aleatoria del diccionario.

            Returns:
                str: Una palabra seleccionada aleatoriamente de la lista de palabras cargadas.
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
