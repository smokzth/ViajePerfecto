class VistaConsola:
    def mostrar_menu_principal(self):
        print ("\n---BIENVENIDO A VIAJE PERFECTO---")
        print("1.Crear nuevo usuario")
        print("2. Ver Itinerarios")
        print("3. salir")

    def solicitar_datos_usuarios(selfself):
        print("\n---Registro de Usuario---")
        nombre=input("Nombre:")
        preferencias=input("Preferencias(separedas por coma):").split(",")
        presupuesto=float(input("Presupusto máximo:"))
        return nombre,[p.strip()for p in preferencias],presupuesto


