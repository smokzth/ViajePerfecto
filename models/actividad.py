class Actividad:
    def __init__(self, nombre: str, descripcion: str, ubicacion: str, costo: float, categoria: str, latitud: float, longitud: float):
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.ubicacion: str = ubicacion
        self.costo: float = costo
        self.categoria: str = categoria
        self.latitud: float = latitud
        self.longitud: float = longitud

    def __str__(self) -> str:
        return f"{self.nombre}  - {self.categoria} - ${self.costo} ({self.ubicacion})"
