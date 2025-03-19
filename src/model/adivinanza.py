class Adivinanza:
    """
    Representa una palabra a adivinar en el juego del ahorcado.

    Attributes:
        __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
        __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
        Inicializa una instancia de la clase Adivinanza, tomando una palabra, la convierte en una lista de letras y
        crea una lista de posiciones inicializadas a False, para llevar el seguimiento
        de qué letras han sido adivinadas.

        Args:
            palabra (str): La palabra que se usará en el juego para ser adivinada.
        """
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> list[int]:
        """
        Intenta adivinar una letra en la palabra. Si la letra está presente, actualiza las posiciones
        correspondientes y devuelve las posiciones donde aparece esa letra.

        Args:
            letra (str): La letra que el jugador intenta adivinar.

        Returns:
            list[int]: Lista de posiciones en las que aparece la letra en la palabra. Si la letra no está,
            devuelve una lista vacía.

        Example:
            >>> adivinanza = Adivinanza("python")
            >>> adivinanza.adivinar('p')
            [0]
            >>> adivinanza.adivinar('a')
            []
        """
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> list[str]:
        """
        Devuelve la lista de letras que conforman la palabra.

        Returns:
            list[str]: Lista de caracteres que representan la palabra original.

        Example:
            >>> adivinanza = Adivinanza("python")
            >>> adivinanza.obtener_letras()
            ['p', 'y', 't', 'h', 'o', 'n']
        """
        return self.__letras

    def obtener_posiciones(self) -> list[bool]:
        """
        Devuelve una lista de booleanos que indican si las letras en las posiciones
        respectivas de la palabra han sido adivinadas.

        Returns:
            list[bool]: Lista de valores booleanos, donde `True` indica que la letra ha sido adivinada,
            y `False` indica que aún no se ha adivinado.

        Example:
            >>> adivinanza = Adivinanza("python")
            >>> adivinanza.obtener_posiciones()
            [False, False, False, False, False, False]
        """
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        """
        Devuelve la cantidad total de posiciones (letras) en la palabra.

        Returns:
            int: La cantidad de letras que tiene la palabra a adivinar.

        Example:
            >>> adivinanza = Adivinanza("python")
            >>> adivinanza.obtener_cantidad_posiciones()
            6
        """
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        """
        Verifica si todas las letras de la palabra han sido adivinadas.

        Returns:
            bool: `True` si todas las letras han sido adivinadas, `False` si alguna letra aún no ha sido adivinada.

        Example:
            >>> adivinanza = Adivinanza("python")
            >>> adivinanza.verificar_si_hay_triunfo()
            False
            >>> adivinanza.adivinar('p')
            [0]
            >>> adivinanza.verificar_si_hay_triunfo()
            False
            >>> adivinanza.adivinar('y')
            [1]
            >>> adivinanza.verificar_si_hay_triunfo()
            False
            >>> adivinanza.adivinar('t')
            [2]
            >>> adivinanza.adivinar('h')
            [3]
            >>> adivinanza.adivinar('o')
            [4]
            >>> adivinanza.adivinar('n')
            [5]
            >>> adivinanza.verificar_si_hay_triunfo()
            True
        """
        return all(self.__posiciones)
