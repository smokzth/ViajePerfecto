from controlers.controlador_principal import ControladorPrincipal
from views.vista_consola import VistaConsola

def main():
    controlador = ControladorPrincipal()
    vista = VistaConsola(controlador)
    vista.iniciar()

if __name__  == "__main__":
    main()
