from src.view.console.menu import Menu
from src.controller.app_controlador import AppControlador

if __name__ == '__main__':
    app_controlador: AppControlador = AppControlador()
    Menu(app_controlador).iniciar()
