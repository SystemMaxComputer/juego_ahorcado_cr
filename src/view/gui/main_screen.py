from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file('src/view/gui/kv/main_screen.kv')


class MainScreen(Screen):
    """
        Representa la pantalla principal de la aplicación de Ahorcado utilizando Kivy.

        Attributes:
            controlador (AppControlador): Instancia del controlador que gestiona la lógica del juego.
    """

    def __init__(self, controlador: AppControlador, **kwargs):
        """
             Inicializa la pantalla principal con una instancia del controlador.

             Args:
                 controlador (AppControlador): Objeto que contiene la lógica del juego.
                 **kwargs: Argumentos adicionales para la inicialización de la clase base Screen.
        """
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def abrir_pantalla_de_configuracion(self):
        """
               Cambia a la pantalla de configuración.
        """
        self.manager.current = 'ConfigScreen'

    def abrir_pantalla_de_juego(self):
        """
               Cambia a la pantalla de juego.
        """
        self.manager.current = 'GameScreen'

    def cerrar_juego(self):
        """
               Cierra la aplicación.
        """
        exit()
