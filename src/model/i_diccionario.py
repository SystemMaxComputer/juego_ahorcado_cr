from abc import ABC


class IDiccionario(ABC):
    def obtener_palabra(self, categoria: str, dificultad: str):
        pass
