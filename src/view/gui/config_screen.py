from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from src.controller.app_controlador import AppControlador

Builder.load_file('src/view/gui/kv/config_screen.kv')


class ConfigScreen(Screen):
    """
    Represents the configuration screen of the Hangman game using Kivy.

    Attributes:
        controlador (AppControlador): Instance of the controller that manages the game logic.
    """

    def __init__(self, controlador: AppControlador, **kwargs):
        """
        Initializes the configuration screen with an instance of the controller.

        Args:
            controlador (AppControlador): Object that contains the game logic.
            **kwargs: Additional arguments for the initialization of the base Screen class.
        """
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def seleccionar_dificultad(self, dificultad):
        """
        Selects the game difficulty and updates the main screen.

        Args:
            dificultad (str): The selected difficulty level.
        """
        print(f"Seleccionando dificultad {dificultad}")
        dificultad_cambiada = self.controlador.modificar_dificultad(dificultad)
        mensaje_de_confirmacion = f"La dificultad ha sido cambiada a {dificultad}" \
            if dificultad_cambiada else "No se pudo cambiar la dificultad"
        self.__mostrar_confirmacion_de_cambio(mensaje_de_confirmacion)
        self.manager.current = 'MainScreen'

    def __mostrar_confirmacion_de_cambio(self, mensaje_de_confirmacion: str):
        """
        Displays a confirmation message after changing the difficulty.

        Args:
            mensaje_de_confirmacion (str): The confirmation message to be displayed.
        """
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text=mensaje_de_confirmacion))
        close_button = Button(text="Cerrar", size_hint=(1, 0.3))
        content.add_widget(close_button)

        popup = Popup(title="Info",
                      content=content)

        close_button.bind(on_press=popup.dismiss)  # Closes the popup
        popup.open()