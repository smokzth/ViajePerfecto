import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime

class VistaGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Viaje Perfecto")
        self.root.geometry("500x600")
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill="both", expand=True)
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_frame()
        ttk.Label(self.frame, text="=== VIAJE PERFECTO ===", font=("Arial", 16, "bold")).pack(pady=10)
        categorias = [
            ("👤 GESTIÓN DE USUARIOS", [
                ("Crear usuario", self.no_implementado),
                ("Cargar usuario existente", self.no_implementado),
                ("Eliminar usuario actual", self.no_implementado),
            ]),
            ("🗺️ GESTIÓN DE ITINERARIOS", [
                ("Crear itinerario", self.no_implementado),
                ("Ver itinerarios disponibles", self.no_implementado),
            ]),
            ("🎯 ACTIVIDADES", [
                ("Agregar actividad a itinerario", self.no_implementado),
                ("Ver actividades de itinerario", self.no_implementado),
                ("Filtrar actividades por categoría", self.no_implementado),
                ("Optimizar rutas de actividades", self.no_implementado),
            ]),
            ("📔 DIARIO DE VIAJE", [
                ("Agregar entrada al diario", self.no_implementado),
                ("Ver entradas del diario", self.no_implementado),
            ]),
            ("💰 GESTIÓN FINANCIERA", [
                ("Ver resumen de gastos", self.no_implementado),
            ]),
            ("📤 EXPORTACIÓN", [
                ("Exportar itinerario", self.no_implementado),
            ]),
        ]

        for seccion, opciones in categorias:
            ttk.Label(self.frame, text=seccion, font=("Arial", 12, "bold")).pack(pady=5)
            for texto, comando in opciones:
                ttk.Button(self.frame, text=texto, command=comando).pack(fill="x", padx=20, pady=2)

        ttk.Button(self.frame, text="Salir", command=self.root.quit).pack(pady=10)

    def solicitar_datos_usuario(self):
        nombre = simpledialog.askstring("Nombre de usuario", "Ingresa tu nombre:")
        preferencias = simpledialog.askstring("Preferencias", "Ingresa tus preferencias separadas por coma:")
        while True:
            try:
                presupuesto = float(simpledialog.askstring("Presupuesto", "Presupuesto máximo:"))
                break
            except:
                messagebox.showerror("Error", "Debes ingresar un número válido.")
        return nombre, [p.strip() for p in preferencias.split(",")], presupuesto

    def mostrar_usuarios(self, usuarios):
        msg = "\n".join(f"{i+1}. {u.nombre} (Itinerarios: {len(u.itinerarios)})" for i, u in enumerate(usuarios))
        messagebox.showinfo("Usuarios registrados", msg or "No hay usuarios.")

    def solicitar_confirmacion(self, mensaje):
        return messagebox.askyesno("Confirmar", mensaje)

    def solicitar_datos_itinerario(self):
        nombre = simpledialog.askstring("Itinerario", "Nombre del itinerario:")
        while True:
            try:
                presupuesto = float(simpledialog.askstring("Presupuesto", "Presupuesto del itinerario:"))
                if presupuesto >= 0:
                    return nombre, presupuesto
                messagebox.showerror("Error", "El presupuesto no puede ser negativo.")
            except:
                messagebox.showerror("Error", "Ingresa un número válido.")

    def mostrar_itinerarios(self, itinerarios):
        if not itinerarios:
            messagebox.showinfo("Itinerarios", "No hay itinerarios registrados.")
        else:
            msg = "\n".join(f"{i+1}. {it.nombre} - Actividades: {len(it.actividades)}" for i, it in enumerate(itinerarios))
            messagebox.showinfo("Itinerarios", msg)

    def solicitar_datos_actividad(self):
        campos = [
            ("Nombre", str), ("Descripción", str), ("Ubicación", str),
            ("Categoría (aventura/cultural/relax)", str), ("Costo", float),
            ("Latitud", float), ("Longitud", float)
        ]
        datos = []
        for campo, tipo in campos:
            while True:
                valor = simpledialog.askstring("Actividad", campo + ":")
                try:
                    datos.append(tipo(valor))
                    break
                except:
                    messagebox.showerror("Error", f"Ingreso inválido para {campo}.")
        return tuple(datos)

    def mostrar_actividades(self, actividades):
        if not actividades:
            messagebox.showinfo("Actividades", "No hay actividades registradas.")
            return
        msg = ""
        for i, a in enumerate(actividades, 1):
            msg += (f"\n{i}. {a.nombre}\n Descripción: {a.descripcion}\n Ubicación: {a.ubicacion}\n"
                    f" Costo: ${a.costo:.2f}\n Categoría: {a.categoria}\n Coordenadas: ({a.latitud}, {a.longitud})\n" + "-"*40)
        messagebox.showinfo("Actividades", msg)

    def solicitar_datos_entrada_diario(self):
        actividad = simpledialog.askstring("Diario", "Nombre de la actividad:")
        while True:
            fecha = simpledialog.askstring("Fecha", "Fecha (YYYY-MM-DD):")
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
                break
            except:
                messagebox.showerror("Error", "Formato inválido. Usa YYYY-MM-DD.")
        nota = simpledialog.askstring("Nota", "Escribe tu nota o experiencia:")
        while True:
            try:
                calificacion = float(simpledialog.askstring("Calificación", "Calificación (0.0 a 5.0):"))
                if 0 <= calificacion <= 5:
                    break
                messagebox.showerror("Error", "Debe estar entre 0.0 y 5.0.")
            except:
                messagebox.showerror("Error", "Ingresa un número válido.")
        ruta_foto = simpledialog.askstring("Foto", "Ruta de la foto (opcional):")
        return actividad, fecha, nota, calificacion, ruta_foto

    def mostrar_diario(self, entradas):
        if not entradas:
            messagebox.showinfo("Diario", "No hay entradas registradas.")
        else:
            msg = ""
            for i, e in enumerate(entradas, 1):
                msg += (f"\n📅 Entrada {i}: {e.actividad} - {e.fecha}\n"
                        f" Nota: {e.nota}\n Calificación: {e.calificacion}/5.0\n"
                        f" Foto: {e.ruta_foto or 'Ninguna'}\n" + "-"*40)
            messagebox.showinfo("Diario de viaje", msg)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Mensaje", mensaje)

    def limpiar_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def no_implementado(self):
        messagebox.showinfo("En desarrollo", "Esta opción aún no está implementada.")

# Para probarla:
if __name__ == "__main__":
    root = tk.Tk()
    app = VistaGrafica(root)
    root.mainloop()


    asda
    asd
    asdasd
    asd
    sda
    asd
    asd
