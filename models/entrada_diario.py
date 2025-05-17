class EntradaDiario:
    def __init__(self, actividad: str, fecha: str, nota: str, calificacion: float, ruta_foto: str):
        self.actividad: str = actividad
        self.fecha: str = fecha  #Formato "YYYY-MM-DD" o similar
        self.nota: str = nota
        self.calificacion: float = calificacion
        self.ruta_foto: str = ruta_foto

    def to_dict(self):
        return {
            "actividad": self.actividad,
            "fecha": self.fecha,
            "nota": self.nota,
            "calificacion": self.calificacion,
            "ruta_foto": self.ruta_foto
        }

    def __str__(self) -> str:
        return f"Entrada para {self.actividad} el {self.fecha}: {self.nota} (Cal: {self.calificacion}, Foto: {self.ruta_foto})"
