import colorama
from colorama import Fore, Style
from src.controller.app_controlador import AppControlador


class Menu:
    """
    Representa el menú principal del juego de adivinanza de palabras.

    Attributes:
        controlador (AppControlador): Instancia del juego que gestiona la lógica de la partida.
    """

    def __init__(self, controlador: AppControlador):
        """
        Inicializa el menú con una instancia de Juego.

        Args:
            controlador (AppControlador): Objeto que contiene la lógica del juego.
        """
        colorama.init(autoreset=True)  # Inicializar colorama para Windows
        self.controlador: AppControlador = controlador

    def __mostrar_opciones(self):
        """
        Muestra las opciones disponibles en el menú principal.
        """
        print(Fore.CYAN + Style.BRIGHT + "🎮 MENÚ PRINCIPAL 🎮\n")
        print(Fore.YELLOW + "1️⃣  Jugar")
        print(Fore.GREEN + "2️⃣  Configuración")
        print(Fore.BLUE + "3️⃣  Salir\n")

    def __pedir_letra(self) -> list[int]:
        """
        Solicita al usuario una letra para adivinar.

        Returns:
            list[int]: Lista con las posiciones donde aparece la letra en la palabra.
        """
        letra = input(Fore.YELLOW + "🎮 ¡Ingresa una letra!: ")
        return self.controlador.adivinar_letra(letra)

    def __modificar_configuracion(self):
        """
        Permite al usuario cambiar la dificultad del juego.
        """
        print(Fore.GREEN + "1️⃣  Dificultad Baja")
        print(Fore.GREEN + "2️⃣  Dificultad Media")
        print(Fore.GREEN + "3️⃣  Dificultad Alta")
        opcion = input(Fore.YELLOW + "🎮 ¡Selecciona la dificultad con la que deseas jugar!: ")

        if opcion == "1":
            self.controlador.modificar_dificultad("facil")
        elif opcion == "2":
            self.controlador.modificar_dificultad("medio")
        elif opcion == "3":
            self.controlador.modificar_dificultad("dificil")

    def __controlar_opcion_1(self):
        """
        Controla el flujo del juego cuando el usuario selecciona la opción de jugar.
        """
        cantidad_posiciones = self.controlador.iniciar_partida()
        display = Fore.RED + " _ " * cantidad_posiciones
        print(display)

        while True:
            if self.controlador.verificar_si_hay_triunfo():
                print(Fore.GREEN + "🎮 ¡Felicitaciones! ¡Has ganado!")
                break
            if not self.controlador.verificar_si_hay_intentos():
                print(Fore.RED + "🎮 ¡Lo siento! ¡Has superado el máximo de intentos!")
                break

            intentos_permitidos = self.controlador.obtener_intentos_permitidos()
            intentos_realizados = intentos_permitidos - self.controlador.obtener_intentos_realizados()
            letra = input(Fore.YELLOW + f"🎮 ¡Ingresa una letra! ({intentos_realizados}/{intentos_permitidos}) ").upper()
            resultado_adivinanza = self.controlador.adivinar_letra(letra)
            self.__mostrar_resultado_jugada(resultado_adivinanza)

    def __mostrar_adivinanza(self):
        """
        Muestra el estado actual de la palabra a adivinar, revelando las letras acertadas.
        """
        letras = self.controlador.obtener_letras()
        posiciones = self.controlador.obtener_posiciones()
        display = ""
        for i in range(len(letras)):
            if posiciones[i]:
                display += Fore.GREEN + " " + letras[i] + " "
            else:
                display += Fore.RED + " _ "

        print(display)

    def __mostrar_resultado_jugada(self, resultado_adivinanza: list[int]):
        """
        Muestra el resultado de la jugada del usuario.

        Args:
            resultado_adivinanza (list[int]): Lista con las posiciones donde aparece la letra en la palabra.
        """
        if len(resultado_adivinanza) == 0:
            print(Fore.YELLOW + "¡Lo siento, no has acertado! ¡Sigue intentando!")
        else:
            print(Fore.YELLOW + "¡Muy bien, has acertado! ¡Sigue así!")
        self.__mostrar_adivinanza()

    def iniciar(self):
        """
        Inicia el menú del juego y gestiona las opciones seleccionadas por el usuario.
        """
        while True:
            self.__mostrar_opciones()
            opcion = input(Fore.MAGENTA + "👉 Selecciona una opción: ")

            if opcion == "1":
                print(Fore.YELLOW + "🎮 ¡Comenzando el juego!")
                self.__controlar_opcion_1()
            elif opcion == "2":
                print(Fore.GREEN + "⚙️  Abriendo configuración...")
                self.__modificar_configuracion()
            elif opcion == "3":
                exit()
            else:
                print(Fore.RED + "❌ Opción no válida, intenta de nuevo.")
