from models.actividad import Actividad
from models.usuario import Usuario
from models.itinerario import  Itinerario
from views.vista_consola import VistaConsola
from models.entrada_diario import EntradaDiario
from utils.persistencia import guardar_usuario

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

            elif opcion == "3":
                if self.usuario:
                    self.crear_itinerario()
                else:
                    self.vista.mostrar_mensaje("Primero debes crear un usuario.")

            elif opcion == "4":
                if self.usuario and self.usuario.itinerarios:
                    self.agregar_actividad_a_itinerario()

                else:
                    self.vista.mostrar_mensaje(" Debes crear un usuario e itinerario primero. ")

            elif opcion == "5":
                self.ver_actividades_de_itinerario()

            elif opcion == "6":
                self.agregar_entrada_diario()

            elif opcion == "7":
                self.ver_entradas_diario()

            elif opcion == "8":
                self.vista.mostrar_mensaje("¡Graciar por usar Viaje Perfecto! ")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente de nuevo. ")

    def crear_usuario(self):
        nombre, preferencias, presupuesto = self.vista.solicitar_datos_usuario()
        self.usuario = Usuario(nombre, preferencias, presupuesto, [])
        guardar_usuario(self.usuario)
        self.vista.mostrar_mensaje(f"Usuario: {nombre} creado exitosamente.")

    def crear_itinerario(self):
        nombre, presupuesto = self.vista.solicitar_datos_itinerario()
        nuevo_itinerario = Itinerario(nombre, self.usuario.nombre, [], [])
        self.usuario.itinerarios.append(nuevo_itinerario)
        self.vista.mostrar_mensaje(f"Itinerario: {nombre } creado exitosamente.")

    def agregar_actividad_a_itinerario(self):
        self.vista.mostrar_mensaje("\n--- Itinerarios Disponibles ---")
        for idx, itinerario in enumerate(self.usuario.itinerarios):
            print (f" {idx + 1}. {itinerario.nombre}")

        seleccion = int(input("Selecciona el número del itinerario ")) -1

        if 0 <= seleccion < len(self.usuario.itinerarios):
            itinerario = self.usuario.itinerarios[seleccion]

            datos = self.vista.solicitar_datos_actividad()
            nueva_actividad = Actividad(*datos)

            itinerario.agregar_actividad(nueva_actividad)
            self.vista.mostrar_mensaje(f"Actividad {nueva_actividad.nombre} agregada a {itinerario.nombre}. ")
        else:
            self.vista.mostrar_mensaje("Selección no válida.")

    def ver_actividades_de_itinerario(self):
        if self.usuario and self.usuario.itinerarios:
            itinerario = self.vista.seleccionar_itinerario(self.usuario.itinerarios)
            self.vista.mostrar_actividades(itinerario.actividades)
        else:
            self.vista.mostrar_mensaje("Debes crear un usuario e itinerario primero.")

    def agregar_entrada_diario(self):
        if not self.usuario or not self.usuario.itinerarios:
            print("\n Debes crear un usuario e itinerario primero.")
            return

        itinerario = self.vista.seleccionar_itinerario(self.usuario.itinerarios)
        if itinerario:
            actividad, fecha, nota, calificacion, ruta_foto = self.vista.solicitar_datos_entrada_diario()
            nueva_entrada = EntradaDiario(actividad, fecha, nota, calificacion, ruta_foto)
            itinerario.diario.append(nueva_entrada)
            print("\nEntrada agregada al diario correctamente.")

    def ver_entradas_diario(self):
        if not self.usuario or not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("Debes crear un usuario e itinerario primero.")
            return

        itinerario = self.vista.seleccionar_itinerario(self.usuario.itinerarios)
        if itinerario:
            self.vista.mostrar_diario(itinerario.diario)
