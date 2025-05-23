from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from src.controller.app_controlador import AppControlador

Builder.load_file('src/view/gui/kv/game_screen.kv')


class GameScreen(Screen):
    """
      Representa la pantalla del juego de Ahorcado utilizando Kivy.

      Attributes:
          controlador (AppControlador): Instancia del controlador que gestiona la lógica del juego.
    """

    def __init__(self, controlador: AppControlador, **kwargs):
        """
                Inicializa la pantalla del juego con una instancia del controlador.

                Args:
                    controlador (AppControlador): Objeto que contiene la lógica del juego.
                    **kwargs: Argumentos adicionales para la inicialización de la clase base Screen.
        """
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
        self.__reiniciar_display()

    def comprobar_letra(self):
        """
               Comprueba la letra ingresada por el usuario y actualiza la pantalla del juego.
        """
        letra = self.ids.letra_input.text
        if len(letra) == 1:
            posiciones = self.controlador.adivinar_letra(letra)
            self.__actualizar_display(posiciones, letra)
            self.ids.letra_input.text = ""
            self.__actualizar_info_intentos()
        else:
            self.__mostrar_mensaje_de_error_por_muchas_letras()

        if not self.controlador.verificar_si_hay_intentos():
            self.__mostrar_fin_juego()

        if self.controlador.verificar_si_hay_triunfo():
            self.__mostrar_felicitaciones_por_triunfo()

    def on_enter(self):
        """
               Método llamado cuando la pantalla se muestra. Inicializa la partida y actualiza la información de intentos.
        """
        self.__reiniciar_display()

    def __actualizar_info_intentos(self):
        """
                Actualiza la información de los intentos restantes en la pantalla.
        """
        intentos_permitidos = self.controlador.obtener_intentos_permitidos()
        intentos_realizados = self.controlador.obtener_intentos_realizados()
        self.ids.info_layout.children[
            0].text = f"Intentos restantes: {intentos_permitidos - intentos_realizados}/{intentos_permitidos}"

    def __reiniciar_display(self):
        """
               Reinicia el display de la palabra a adivinar en la pantalla.
        """
        numero_de_letras = self.controlador.iniciar_partida()
        self.ids.palabra_layout.clear_widgets()
        for _ in range(numero_de_letras):
            letra = Label(text="_", font_size=50)
            self.ids.palabra_layout.add_widget(letra)
        self.__actualizar_info_intentos()

    def __actualizar_display(self, posiciones: list[int], letra: str):
        """
               Actualiza el display de la palabra a adivinar con las letras acertadas.

               Args:
                   posiciones (list[int]): Lista con las posiciones donde aparece la letra en la palabra.
                   letra (str): Letra acertada.
        """
        for pos in posiciones:
            self.ids.palabra_layout.children[-1 * (pos + 1)].text = letra.upper()

    def __mostrar_felicitaciones_por_triunfo(self):
        """
               Muestra un mensaje de felicitaciones por haber ganado el juego.
        """
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text="Felicitaciones ¡Has Ganado!"))
        close_button = Button(text="Cerrar", size_hint=(1, 0.3))
        content.add_widget(close_button)

        popup = Popup(title="Info",
                      content=content)

        close_button.bind(on_press=popup.dismiss)  # Cierra el popup
        popup.open()
        self.manager.current = 'MainScreen'

    def __mostrar_fin_juego(self):
        """
              Muestra un mensaje de fin de juego por haber perdido.
        """
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text="Lo sentimos, ¡has perdido!"))
        close_button = Button(text="Cerrar", size_hint=(1, 0.3))
        content.add_widget(close_button)

        popup = Popup(title="Info",
                      content=content)

        close_button.bind(on_press=popup.dismiss)  # Cierra el popup
        popup.open()
        self.manager.current = 'MainScreen'

    def __mostrar_mensaje_de_error_por_muchas_letras(self):
        """
               Muestra un mensaje de error cuando se ingresa más de una letra.
        """
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text="Ingresaste mas de una letra"))
        close_button = Button(text="Cerrar", size_hint=(1, 0.3))
        content.add_widget(close_button)

        popup = Popup(title="Error",
                      content=content)

        close_button.bind(on_press=popup.dismiss)  # Cierra el popup
        popup.open()
