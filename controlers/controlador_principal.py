from models.actividad import Actividad
from models.usuario import Usuario
from models.itinerario import Itinerario
from models.entrada_diario import EntradaDiario
from views.vista_consola import VistaConsola
from utils.persistencia import cargar_usuarios, eliminar_usuario, guardar_usuario

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
                self.cargar_usuario()
            elif opcion == "3":
                self.eliminar_usuario()
            elif opcion == "4":
                self.crear_itinerario()
            elif opcion == "5":
                self.ver_itinerarios()
            elif opcion == "6":
                self.agregar_actividad_a_itinerario()
            elif opcion == "7":
                self.ver_actividades_de_itinerario()
            elif opcion == "8":
                self.agregar_entrada_diario()
            elif opcion == "9":
                self.ver_entradas_diario()
            elif opcion == "10":
                self.vista.mostrar_mensaje("¡Gracias por usar Viaje Perfecto!")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente de nuevo.")

    # --- Gestión de Usuarios ---
    def crear_usuario(self):
        nombre, preferencias, presupuesto = self.vista.solicitar_datos_usuario()
        self.usuario = Usuario(nombre, preferencias, presupuesto, [])
        guardar_usuario(self.usuario)
        self.vista.mostrar_mensaje(f"Usuario '{nombre}' creado exitosamente.")

    def cargar_usuario(self):
        usuarios = cargar_usuarios()
        if not usuarios:
            self.vista.mostrar_mensaje("No hay usuarios registrados.")
            return

        self.vista.mostrar_usuarios(usuarios)
        try:
            seleccion = int(input("Seleccione un usuario: ")) - 1
            if 0 <= seleccion < len(usuarios):
                self.usuario = usuarios[seleccion]
                self.vista.mostrar_mensaje(f"Usuario '{self.usuario.nombre}' cargado.")
            else:
                self.vista.mostrar_mensaje("Número de usuario inválido.")
        except ValueError:
            self.vista.mostrar_mensaje("Debe ingresar un número válido.")

    def eliminar_usuario(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("Primero cargue un usuario.")
            return

        if self.vista.solicitar_confirmacion(f"¿Eliminar al usuario '{self.usuario.nombre}'?"):
            eliminar_usuario(self.usuario.nombre)
            self.usuario = None
            self.vista.mostrar_mensaje("Usuario eliminado correctamente.")

    # --- Gestión de Itinerarios ---
    def ver_itinerarios(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("Primero debes crear/cargar un usuario.")
            return
        self.vista.mostrar_itinerarios(self.usuario.itinerarios)

    def crear_itinerario(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("Primero debes crear/cargar un usuario.")
            return

        nombre, presupuesto = self.vista.solicitar_datos_itinerario()
        nuevo_itinerario = Itinerario(nombre, self.usuario.nombre, [], [])
        self.usuario.itinerarios.append(nuevo_itinerario)
        guardar_usuario(self.usuario)  # Actualiza el archivo JSON
        self.vista.mostrar_mensaje(f"Itinerario '{nombre}' creado exitosamente.")

    def agregar_actividad_a_itinerario(self):
        if not self.usuario or not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("Debes tener un usuario e itinerario creados.")
            return

        self.vista.mostrar_itinerarios(self.usuario.itinerarios)
        try:
            seleccion = int(input("Seleccione itinerario: ")) - 1
            if 0 <= seleccion < len(self.usuario.itinerarios):
                datos = self.vista.solicitar_datos_actividad()
                nueva_actividad = Actividad(*datos)
                self.usuario.itinerarios[seleccion].agregar_actividad(nueva_actividad)
                guardar_usuario(self.usuario)  # Actualiza el archivo JSON
                self.vista.mostrar_mensaje(f"Actividad '{nueva_actividad.nombre}' agregada.")
            else:
                self.vista.mostrar_mensaje("Selección inválida.")
        except ValueError:
            self.vista.mostrar_mensaje("Debe ingresar un número válido.")

    def ver_actividades_de_itinerario(self):
        if not self.usuario or not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("Debes tener un usuario e itinerario creados.")
            return

        try:
            self.vista.mostrar_itinerarios(self.usuario.itinerarios)
            seleccion = int(input("Seleccione itinerario para ver actividades: ")) - 1
            if 0 <= seleccion < len(self.usuario.itinerarios):
                itinerario = self.usuario.itinerarios[seleccion]
                self.vista.mostrar_actividades(itinerario.actividades)
            else:
                self.vista.mostrar_mensaje("Número de itinerario inválido.")
        except ValueError:
            self.vista.mostrar_mensaje("Debe ingresar un número válido.")


    # --- Gestión de Diario ---
    def agregar_entrada_diario(self):
        if not self.usuario or not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("Debes tener un usuario e itinerario creados.")
            return

        itinerario = self.vista.seleccionar_itinerario(self.usuario.itinerarios)
        if itinerario:
            datos = self.vista.solicitar_datos_entrada_diario()
            nueva_entrada = EntradaDiario(*datos)
            itinerario.diario.append(nueva_entrada)
            guardar_usuario(self.usuario)  # Actualiza el archivo JSON
            self.vista.mostrar_mensaje("Entrada agregada al diario.")

    def ver_entradas_diario(self):
        if not self.usuario or not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("Debes tener un usuario e itinerario creados.")
            return

        try:
            self.vista.mostrar_itinerarios(self.usuario.itinerarios)
            seleccion = int(input("Seleccione itinerario para ver el diario: ")) - 1
            if 0 <= seleccion < len(self.usuario.itinerarios):
                itinerario = self.usuario.itinerarios[seleccion]
                self.vista.mostrar_diario(itinerario.diario)
            else:
                self.vista.mostrar_mensaje("Número de itinerario inválido.")
        except ValueError:
            self.vista.mostrar_mensaje("Debe ingresar un número válido.")