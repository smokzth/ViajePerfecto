class VistaConsola:
    def mostrar_menu_principal(self):
        print("\n--- BIENVENIDO A VIAJE PERFECTO ---")
        print("1. Crear nuevo usuario")
        print("2. Ver itinerarios")
        print("3. Crear itinerario")
        print("4. Agregar actividad a itinerario")
        print("5. Salir")

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

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")
