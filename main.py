from controlers.controlador_principal import ControladorPrincipal
from views.vista_tkinter import VistaTkinter  # Asume que guardaste la clase VistaTkinter en este archivo


def main():
    # Crea la instancia del controlador
    controlador = ControladorPrincipal()

    # Crea la vista gráfica pasando el controlador
    vista = VistaTkinter(controlador)

    # Establece la vista en el controlador (para comunicación bidireccional)
    controlador.vista = vista

    # Inicia la aplicación
    vista.iniciar()


if __name__ == "__main__":
    main()