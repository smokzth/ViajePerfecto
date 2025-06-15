from models.actividad import Actividad
from models.usuario import Usuario
from models.itinerario import Itinerario
from models.entrada_diario import EntradaDiario
from views.vista_consola import VistaConsola
from utils.persistencia import cargar_usuarios, eliminar_usuario, guardar_usuario
from utils.optimizador_rutas import optimizar_ruta
from utils.exportador import exportar_itinerario


class ControladorPrincipal:
    def __init__(self):
        self.vista = None
        self.usuario = None

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            # Gestión de Usuarios
            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.cargar_usuario()
            elif opcion == "3":
                self.eliminar_usuario()

            # Gestión de Itinerarios
            elif opcion == "4":
                self.crear_itinerario()
            elif opcion == "5":
                self.ver_itinerarios()

            # Gestión de Actividades
            elif opcion == "6":
                self.agregar_actividad_a_itinerario()
            elif opcion == "7":
                self.ver_actividades_de_itinerario()
            elif opcion == "8":
                self.filtrar_actividades_por_categoria()
            elif opcion == "9":
                self.optimizar_rutas_actividades()

            # Diario de Viaje
            elif opcion == "10":
                self.agregar_entrada_diario()
            elif opcion == "11":
                self.ver_entradas_diario()

            # Gestión Financiera
            elif opcion == "12":
                self.mostrar_resumen_gastos()

            # Exportación
            elif opcion == "13":
                self.exportar_itinerario()

            # Salir
            elif opcion == "0":
                self.vista.mostrar_mensaje("¡Gracias por usar Viaje Perfecto!")
                break

            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente de nuevo.")

    # --- Gestión de Usuarios ---
    def crear_usuario(self):
        nombre, preferencias, presupuesto = self.vista.solicitar_datos_usuario()
        self.usuario = Usuario(nombre, preferencias, presupuesto, [])
        guardar_usuario(self.usuario)
        self.vista.mostrar_mensaje(f"✅ Usuario '{nombre}' creado exitosamente.")

    def cargar_usuario(self):
        usuarios = cargar_usuarios()
        if not usuarios:
            self.vista.mostrar_mensaje("⚠️ No hay usuarios registrados.")
            return

        self.vista.mostrar_usuarios(usuarios)
        try:
            seleccion = int(input("Seleccione un usuario: ")) - 1
            if 0 <= seleccion < len(usuarios):
                self.usuario = usuarios[seleccion]
                self.vista.mostrar_mensaje(f"✅ Usuario '{self.usuario.nombre}' cargado.")
            else:
                self.vista.mostrar_mensaje("❌ Número de usuario inválido.")
        except ValueError:
            self.vista.mostrar_mensaje("❌ Debe ingresar un número válido.")

    def eliminar_usuario(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("⚠️ Primero cargue un usuario.")
            return

        if self.vista.solicitar_confirmacion(f"¿Eliminar al usuario '{self.usuario.nombre}'?"):
            eliminar_usuario(self.usuario.nombre)
            self.usuario = None
            self.vista.mostrar_mensaje("✅ Usuario eliminado correctamente.")

    # --- Gestión de Itinerarios ---
    def crear_itinerario(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("⚠️ Primero debes crear/cargar un usuario.")
            return

        nombre, presupuesto = self.vista.solicitar_datos_itinerario()
        nuevo_itinerario = Itinerario(
            nombre=nombre,
            usuario=self.usuario.nombre,
            actividades=[],
            diario=[],
            presupuesto=presupuesto  # Añade el presupuesto aquí
        )
        self.usuario.itinerarios.append(nuevo_itinerario)
        guardar_usuario(self.usuario)
        self.vista.mostrar_mensaje(f"✅ Itinerario '{nombre}' creado exitosamente.")

    def ver_itinerarios(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("⚠️ Primero debes crear/cargar un usuario.")
            return
        self.vista.mostrar_itinerarios(self.usuario.itinerarios)

    # --- Gestión de Actividades ---
    def agregar_actividad_a_itinerario(self):
        if not self._validar_usuario_y_itinerarios():
            return

        try:
            itinerario = self._seleccionar_itinerario()
            if not itinerario:
                return

            datos = self.vista.solicitar_datos_actividad()
            nueva_actividad = Actividad(*datos)

            if not self.verificar_presupuesto(itinerario, nueva_actividad.costo):
                self.vista.mostrar_mensaje("❌ El costo excede el presupuesto del itinerario.")
                return

            itinerario.agregar_actividad(nueva_actividad)
            guardar_usuario(self.usuario)
            self.vista.mostrar_mensaje(f"✅ Actividad '{nueva_actividad.nombre}' agregada.")

        except ValueError as e:
            self.vista.mostrar_mensaje(f"❌ Error: {str(e)}")

    def ver_actividades_de_itinerario(self):
        if not self._validar_usuario_y_itinerarios():
            return

        itinerario = self._seleccionar_itinerario()
        if itinerario:
            self.vista.mostrar_actividades(itinerario.actividades)

    def filtrar_actividades_por_categoria(self):
        if not self._validar_usuario_y_itinerarios():
            return

        categoria = input("Ingrese categoría a filtrar (aventura/cultural/relax): ").lower()
        actividades_filtradas = []

        for itinerario in self.usuario.itinerarios:
            for actividad in itinerario.actividades:
                if actividad.categoria.lower() == categoria:
                    actividades_filtradas.append((itinerario.nombre, actividad))

        if actividades_filtradas:
            print(f"\n🎯 Actividades de categoría '{categoria}':")
            for itinerario, actividad in actividades_filtradas:
                print(f"\n📌 Itinerario: {itinerario}")
                print(f"   Nombre: {actividad.nombre}")
                print(f"   Ubicación: {actividad.ubicacion}")
                print(f"   Costo: ${actividad.costo:.2f}")
        else:
            self.vista.mostrar_mensaje(f"❌ No hay actividades de categoría '{categoria}'")

    def optimizar_rutas_actividades(self):
        if not self._validar_usuario_y_itinerarios():
            return

        itinerario = self._seleccionar_itinerario()
        if itinerario and itinerario.actividades:
            actividades_optimizadas = optimizar_ruta(itinerario.actividades)
            itinerario.actividades = actividades_optimizadas
            guardar_usuario(self.usuario)
            self.vista.mostrar_mensaje("✅ Ruta optimizada correctamente.")
            self.vista.mostrar_actividades(itinerario.actividades)

    # --- Diario de Viaje ---
    def agregar_entrada_diario(self):
        if not self._validar_usuario_y_itinerarios():
            return

        itinerario = self._seleccionar_itinerario()
        if itinerario:
            datos = self.vista.solicitar_datos_entrada_diario()
            nueva_entrada = EntradaDiario(*datos)
            itinerario.diario.append(nueva_entrada)
            guardar_usuario(self.usuario)
            self.vista.mostrar_mensaje("✅ Entrada agregada al diario.")

    def ver_entradas_diario(self):
        if not self._validar_usuario_y_itinerarios():
            return

        itinerario = self._seleccionar_itinerario()
        if itinerario:
            self.vista.mostrar_entradas_diario(itinerario.diario)

    # --- Gestión Financiera ---
    def mostrar_resumen_gastos(self):
        if not self._validar_usuario_y_itinerarios():
            return

        for itinerario in self.usuario.itinerarios:
            total = sum(act.costo for act in itinerario.actividades)
            disponible = itinerario.presupuesto - total
            self.vista.mostrar_mensaje(
                f"💰 Itinerario: {itinerario.nombre}\n"
                f"   Gastado: ${total:.2f} / Presupuesto: ${itinerario.presupuesto:.2f}\n"
                f"   Disponible: ${disponible:.2f}"
            )

    # --- Exportación ---
    def exportar_itinerario(self):
        if not self._validar_usuario_y_itinerarios():
            return

        itinerario = self._seleccionar_itinerario()
        if itinerario:
            nombre_archivo = exportar_itinerario(itinerario)
            self.vista.mostrar_mensaje(f"✅ Itinerario exportado como '{nombre_archivo}'")

    # --- Métodos auxiliares ---
    def _validar_usuario_y_itinerarios(self):
        if not self.usuario:
            self.vista.mostrar_mensaje("⚠️ Primero debes crear/cargar un usuario.")
            return False
        if not self.usuario.itinerarios:
            self.vista.mostrar_mensaje("⚠️ No hay itinerarios creados.")
            return False
        return True

    def _seleccionar_itinerario(self):
        self.vista.mostrar_itinerarios(self.usuario.itinerarios)
        try:
            seleccion = int(input("Seleccione itinerario: ")) - 1
            if 0 <= seleccion < len(self.usuario.itinerarios):
                return self.usuario.itinerarios[seleccion]
            self.vista.mostrar_mensaje("❌ Selección inválida.")
        except ValueError:
            self.vista.mostrar_mensaje("❌ Debe ingresar un número válido.")
        return None

    def verificar_presupuesto(self, itinerario, costo_actividad):
        total_gastado = sum(act.costo for act in itinerario.actividades)
        return (total_gastado + costo_actividad) <= itinerario.presupuesto