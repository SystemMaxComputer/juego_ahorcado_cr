class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> list[int]:
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> list[str]:
        return self.__letras

    def obtener_posiciones(self) -> list[bool]:
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        return all(self.__posiciones)
