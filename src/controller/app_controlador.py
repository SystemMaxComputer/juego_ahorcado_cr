from src.model.juego import Juego
from src.model.diccionario_file import DiccionarioFile
from src.model.diccionario_bd import DiccionarioBD


class AppControlador:
    def __init__(self):
        self.juego = Juego(DiccionarioFile())
        # self.juego = Juego(DiccionarioBD())

    def iniciar_partida(self):
        return self.juego.iniciar_partida()

    def obtener_intentos_permitidos(self) -> int:
        return self.juego.calcular_intentos_permitidos()

    def obtener_posiciones(self) -> list[bool]:
        return self.juego.obtener_adivinanza().obtener_posiciones()

    def obtener_letras(self) -> list[str]:
        return self.juego.obtener_adivinanza().obtener_letras()

    def obtener_intentos_realizados(self) -> int:
        return self.juego.obtener_intentos_realizados()

    def verificar_si_hay_intentos(self) -> bool:
        return self.juego.verificar_si_hay_intentos()

    def verificar_si_hay_triunfo(self) -> bool:
        return self.juego.verificar_triunfo()

    def adivinar_letra(self, letra: str) -> list[int]:
        return self.juego.adivinar(letra.upper())

    def modificar_dificultad(self, dificultad: str) -> bool:
        if dificultad == "facil":
            self.juego.modificar_dificultad(self.juego.DIFICULTAD_BAJA)
            return True
        if dificultad == "medio":
            self.juego.modificar_dificultad(self.juego.DIFICULTAD_MEDIA)
            return True
        if dificultad == "dificil":
            self.juego.modificar_dificultad(self.juego.DIFICULTAD_ALTA)
            return True
        return False
