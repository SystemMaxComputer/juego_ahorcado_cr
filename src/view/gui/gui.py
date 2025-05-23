from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.controller.app_controlador import AppControlador
from src.view.gui.config_screen import ConfigScreen
from src.view.gui.game_screen import GameScreen
from src.view.gui.main_screen import MainScreen


class AhorcadoApp(App):
    """
     Representa la aplicación principal del juego de Ahorcado utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """

    def __init__(self, controlador: AppControlador, **kwargs):
        """
              Inicializa la aplicación con una instancia del controlador.

              Args:
                  controlador (AppControlador): Objeto que contiene el controlador.
                  **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def build(self):
        """
               Construye y retorna el administrador de pantallas de la aplicación.

               Returns:
                   ScreenManager: Administrador de pantallas que maneja las diferentes vistas de la aplicación.
        """
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="MainScreen", controlador=self.controlador))
        screen_manager.add_widget(ConfigScreen(name="ConfigScreen", controlador=self.controlador))
        screen_manager.add_widget(GameScreen(name="GameScreen", controlador=self.controlador))
        return screen_manager
