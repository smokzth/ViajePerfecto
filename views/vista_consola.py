from datetime import datetime

class VistaConsola:
    def mostrar_menu_principal(self):
        """Muestra el menú principal con todas las opciones disponibles"""
        print("\n=== VIAJE PERFECTO ===")
        print("═" * 25)
        print("👤 GESTIÓN DE USUARIOS")
        print("1. Crear usuario")
        print("2. Cargar usuario existente")
        print("3. Eliminar usuario actual")
        print("═" * 25)
        print("🗺️ GESTIÓN DE ITINERARIOS")
        print("4. Crear itinerario")
        print("5. Ver itinerarios disponibles")
        print("═" * 25)
        print("🎯 ACTIVIDADES")
        print("6. Agregar actividad a itinerario")
        print("7. Ver actividades de itinerario")
        print("8. Filtrar actividades por categoría")
        print("9. Optimizar rutas de actividades")
        print("═" * 25)
        print("📔 DIARIO DE VIAJE")
        print("10. Agregar entrada al diario")
        print("11. Ver entradas del diario")
        print("═" * 25)
        print("💰 GESTIÓN FINANCIERA")
        print("12. Ver resumen de gastos")
        print("═" * 25)
        print("📤 EXPORTACIÓN")
        print("13. Exportar itinerario")
        print("═" * 25)
        print("0. Salir")
        print("═" * 25)

    # --- Métodos para Usuarios ---
    def solicitar_datos_usuario(self):
        """Solicita los datos necesarios para crear un nuevo usuario"""
        print("\n--- Registro de Usuario ---")
        nombre = input("Nombre: ")
        preferencias = [p.strip() for p in input("Preferencias (separadas por coma): ").split(",")]
        while True:
            try:
                presupuesto = float(input("Presupuesto máximo: $"))
                break
            except ValueError:
                print("❌ Entrada inválida. Ingresa un número válido para el presupuesto.")
        return nombre, preferencias, presupuesto

    def mostrar_usuarios(self, usuarios):
        """Muestra la lista de usuarios disponibles"""
        print("\n--- USUARIOS REGISTRADOS ---")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. {usuario.nombre} (Itinerarios: {len(usuario.itinerarios)})")

    def solicitar_confirmacion(self, mensaje):
        """Solicita confirmación al usuario (s/n)"""
        return input(f"\n{mensaje} (s/n): ").lower() == "s"

    # --- Métodos para Itinerarios ---
    def solicitar_datos_itinerario(self):
        print("\n--- Crear Itinerario ---")
        nombre = input("Nombre del itinerario: ")
        while True:
            try:
                presupuesto = float(input("Presupuesto del itinerario: $"))
                if presupuesto >= 0:
                    return nombre, presupuesto
                print("❌ El presupuesto no puede ser negativo")
            except ValueError:
                print("❌ Ingrese un número válido")

    def mostrar_itinerarios(self, itinerarios):
        """Muestra la lista de itinerarios disponibles"""
        print("\n--- ITINERARIOS ---")
        if not itinerarios:
            print("No hay itinerarios registrados.")
        else:
            for i, itinerario in enumerate(itinerarios, 1):
                print(f"{i}. {itinerario.nombre} - Actividades: {len(itinerario.actividades)}")

    def seleccionar_itinerario(self, itinerarios):
        """Permite seleccionar un itinerario de la lista"""
        self.mostrar_itinerarios(itinerarios)
        try:
            opcion = int(input("\nNúmero del itinerario: ")) - 1
            return itinerarios[opcion] if 0 <= opcion < len(itinerarios) else None
        except ValueError:
            return None

    # --- Métodos para Actividades ---
    def solicitar_datos_actividad(self):
        """Solicita los datos necesarios para agregar una actividad"""
        print("\n--- Agregar Actividad ---")
        nombre = input("Nombre de la actividad: ")
        descripcion = input("Descripción: ")
        ubicacion = input("Ubicación: ")
        categoria = input("Categoría (aventura/cultural/relax): ")

        while True:
            try:
                costo = float(input("Costo: $"))
                break
            except ValueError:
                print("❌ Ingresa un valor numérico válido para el costo.")

        while True:
            try:
                latitud = float(input("Latitud: "))
                break
            except ValueError:
                print("❌ Ingresa un valor numérico válido para la latitud.")

        while True:
            try:
                longitud = float(input("Longitud: "))
                break
            except ValueError:
                print("❌ Ingresa un valor numérico válido para la longitud.")

        return nombre, descripcion, ubicacion, costo, categoria, latitud, longitud

    def mostrar_actividades(self, actividades):
        """Muestra la lista de actividades de un itinerario"""
        print("\n--- ACTIVIDADES ---")
        if not actividades:
            print("No hay actividades registradas.")
        else:
            for i, actividad in enumerate(actividades, 1):
                print(f"\n{i}. {actividad.nombre}")
                print(f"   Descripción: {actividad.descripcion}")
                print(f"   Ubicación: {actividad.ubicacion}")
                print(f"   Costo: ${actividad.costo:.2f}")
                print(f"   Categoría: {actividad.categoria}")
                print(f"   Coordenadas: ({actividad.latitud}, {actividad.longitud})")
                print("-" * 40)

    # --- Métodos para Diario ---
    def solicitar_datos_entrada_diario(self):
        """Solicita los datos necesarios para agregar una entrada al diario"""
        print("\n--- Agregar Entrada al Diario ---")
        actividad = input("Nombre de la actividad: ")

        while True:
            fecha = input("Fecha (YYYY-MM-DD): ")
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
                break
            except ValueError:
                print("❌ Fecha inválida. Usa el formato YYYY-MM-DD (ejemplo: 2025-05-20).")

        nota = input("Escribe tu nota o experiencia: ")

        while True:
            try:
                calificacion = float(input("Calificación (0.0 a 5.0): "))
                if 0 <= calificacion <= 5:
                    break
                print("La calificación debe estar entre 0.0 y 5.0")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        ruta_foto = input("Ruta de la foto (opcional): ")
        return actividad, fecha, nota, calificacion, ruta_foto

    def mostrar_diario(self, entradas):
        """Muestra las entradas del diario de viaje"""
        print("\n--- DIARIO DE VIAJE ---")
        if not entradas:
            print("No hay entradas registradas.")
        else:
            for i, entrada in enumerate(entradas, 1):
                print(f"\n📅 Entrada {i}: {entrada.actividad} - {entrada.fecha}")
                print(f"   Nota: {entrada.nota}")
                print(f"   Calificación: {entrada.calificacion}/5.0")
                if entrada.ruta_foto:
                    print(f"   Foto: {entrada.ruta_foto}")
                print("-" * 40)

    def mostrar_resumen_gastos(self):
        if not self._validar_usuario_y_itinerarios():
            return

        for itinerario in self.usuario.itinerarios:
            total = sum(act.costo for act in itinerario.actividades)
            disponible = itinerario.presupuesto - total
            self.vista.mostrar_mensaje(
                f"\n💰 ITINERARIO: {itinerario.nombre.upper()}\n"
                f"   Presupuesto total: ${itinerario.presupuesto:.2f}\n"
                f"   Gastos realizados: ${total:.2f}\n"
                f"   Saldo disponible: ${disponible:.2f}\n"
                f"   Porcentaje utilizado: {(total / itinerario.presupuesto) * 100:.1f}%"
            )


    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje genérico al usuario"""
        print(f"\nℹ️ {mensaje}")

