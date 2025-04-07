from models.usuario import Usuario
from models.itinerario import  Itinerario
from views.vista_consola import VistaConsola

class ControladorPrincipal:
    def __init__(self):
        self.vista = VistaConsola()
        self.usuario = None

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_usuario()

            elif opcion == "2":
                if self.usuario:
                    self.vista.mostrar_itinerarios(self.usuario.itinerarios)
                else:
                    self.vista.mostrar_mensaje("Primero debes crear un usuario.")

            elif opcion == "2":
                self.vista.mostrar_mensaje("¡Graciar por usar Viaje Perfecto! ")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente de nuevo. ")
    def crear_usuario(self):
        nombre, preferencias, presupuesto = self.vista.solicitar_datos_usuario()
        self.usuario = Usuario(nombre, preferencias, presupuesto, [])
        self.vista.mostrar_mensaje(f"Usuario: {nombre} creado exitosamente. ")