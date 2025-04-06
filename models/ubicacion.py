class Ubicacion:
    def __init__(self, ciudad: str, pais: str, latitud: float, longitud: float):
        self.ciudad: str = ciudad
        self.pais: str = pais
        self.latitud: float = latitud
        self.longitud: float = longitud

    def __str__(self) -> str:
        return f"{self.ciudad}, {self.pais} (Lat: {self.latitud}, Lon: {self.longitud})"


