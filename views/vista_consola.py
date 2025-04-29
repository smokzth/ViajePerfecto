class VistaConsola:
    def mostrar_menu_principal(self):
        print("\n--- BIENVENIDO A VIAJE PERFECTO ---")
        print("1. Crear nuevo usuario.")
        print("2. Ver itinerarios.")
        print("3. Crear itinerario.")
        print("4. Agregar actividad a itinerario.")
        print("5. Ver actividades de un itinerario.")
        print("6. Agregar entrada al diario de viaje.")
        print("7. Ver entradas del diario.")
        print("8. Sair.")

    def solicitar_datos_usuario(self):
        print("\n--- Registro de Usuario ---")
        nombre = input("Nombre: ")
        preferencias = input("Preferencias (separadas por coma): ").split(",")
        presupuesto = float(input("Presupuesto máximo: "))
        return nombre, [p.strip() for p in preferencias], presupuesto

    def solicitar_datos_itinerario(self):
        print("\n---Crear Itinerario:---")
        nombre=input("Nombre del itinerario:")
        presupuesto=float(input("Presupuesto del itinerario"))
        return nombre, presupuesto

    def mostrar_itinerarios(self, itinerarios):
        print("\n--- Itinerarios ---")
        if not itinerarios:
            print("No hay itinerarios Registrados.")
        else:
            for i, it in enumerate(itinerarios, 1):
                print(f"{i}. {it.nombre} - Actividades: {len(it.actividades)}")

    def solicitar_datos_actividad(self):
        print("\n--- Agregar actividad ---")
        nombre= input("Nombre de la actividad: ")
        descripcion= input("Descripción: ")
        ubicacion= input("Ubicación: ")
        costo= float(input("Costo: "))
        categoria= input("Categoría (ej: aventura, cultural, relax): ")
        latitud= float(input("Latitud: "))
        longitud= float(input("Longitud: "))
        return nombre, descripcion, ubicacion, costo, categoria, latitud, longitud

    def seleccionar_itinerario(self, itinerarios):
        print("\n--- Selecciona un itinerario ---")
        for idx, itinerario in enumerate(itinerarios):
            print(f"{idx +1}. {itinerario.nombre}")
        opcion = int(input("Número del itinerario: ")) - 1
        return itinerarios[opcion]

    def mostrar_actividades(self, actividades):
        print("\n--- Actividades del Itinerario ---")
        if not actividades:
            print("No hay actividades registradas en este itinerario.")
        else:
            for actividad in actividades:
                print(f"📍 Nombre: {actividad.nombre}")
                print(f"📝 Descripción: {actividad.descripcion}")
                print(f"📍 Ubicación: {actividad.ubicacion}")
                print(f"💰 Costo: ${actividad.costo}")
                print(f"📂 Categoría: {actividad.categoria}")
                print(f"🌐 Coordenadas: ({actividad.latitud}, {actividad.longitud})")
                print("------------------------------------------------")

    def solicitar_datos_entrada_diario(self):
        print("\n--- Agregar entrada al diario ---")
        actividad = input("Nombre de la actividad: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        nota = input("Escribe tu nota o experiencia: ")

        while True:
            try:
                calificacion = float(input("Calificación (0.0 a 5.0): "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")

        ruta_foto = input("Ruta de la foto (opcional): ")
        return actividad, fecha, nota, calificacion, ruta_foto

    def mostrar_diario(self, entradas):
        print("\n--- Diario de Viaje ---")
        if not entradas:
            print("No hay entradas en el diario.")
        else:
            for entrada in entradas:
                print(
                    f"{entrada.fecha} - {entrada.actividad}: {entrada.nota} (Cal: {entrada.calificacion}, Foto: {entrada.ruta_foto})")

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")
