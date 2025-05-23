from src.model.diccionario_bd import DiccionarioBD
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes
from src.model.i_diccionario import IDiccionario


class Juego:
    """
    Representa la lógica de un juego de adivinanza de palabras.

    Attributes:
        DIFICULTAD_BAJA (str): Constante para la dificultad baja (20 intentos).
        DIFICULTAD_MEDIA (str): Constante para la dificultad media (10 intentos).
        DIFICULTAD_ALTA (str): Constante para la dificultad alta (5 intentos).
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self, diccionario: IDiccionario):
        """
            Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_ALTA
        self.__intentos_realizados: int = 0
        self.__diccionario: IDiccionario = diccionario
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self):
        """
            Obtiene la cantidad de intentos restantes.

            Returns:
                int: Número de intentos disponibles.
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
            Obtiene la instancia actual de la adivinanza.

            Returns:
                Adivinanza: Objeto que representa la palabra a adivinar.
        """

        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
            Genera una palabra aleatoria desde el diccionario.

            Returns:
                str: Palabra seleccionada aleatoriamente.
        """
        return self.__diccionario.obtener_palabra("Frutas", "Difícil")

    def calcular_intentos_permitidos(self) -> int:
        """
            Calcula la cantidad de intentos permitidos según la dificultad.

            Returns:
                int: Número de intentos permitidos.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
            Modifica el nivel de dificultad del juego.

            Args:
                dificultad (str): Nueva dificultad a establecer (DIFICULTAD_BAJA, DIFICULTAD_MEDIA, DIFICULTAD_ALTA).
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
            Inicia una nueva partida generando una palabra y estableciendo los intentos permitidos.

            Returns:
                int: Cantidad de letras en la palabra a adivinar.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> list[int]:
        """
            Intenta adivinar una letra de la palabra.

            Args:
                letra (str): Letra que el jugador quiere adivinar.

            Returns:
                list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
            Verifica si quedan intentos disponibles.

            Returns:
                bool: `True` si hay intentos disponibles, `False` si se agotaron.
        """
        print(self.__intentos_realizados)
        return self.__intentos_realizados > 0

    def verificar_triunfo(self) -> bool:
        """
            Verifica si el jugador ha adivinado todas las letras de la palabra.

            Returns:
                bool: `True` si el jugador ha ganado, `False` en caso contrario.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()
