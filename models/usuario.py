from typing import List
from models.itinerario import Itinerario

class Usuario:
    def __init__(self, nombre: str, preferencias: list[str], presupuesto_maximo: float, itinerarios: List[Itinerario]):
        self.nombre: str = nombre
        self.preferencias: list[str] = preferencias
        self.presupuesto_maximo: float = presupuesto_maximo
        self.itinerarios: list[Itinerario] = itinerarios


    def __str__(self):
        return f"Usuario: {self.nombre}, Preferencias: {', '.join(self.preferencias)}, Presupuesto: ${self.presupuesto_maximo}"

