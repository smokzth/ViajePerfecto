from typing import List
from models.itinerario import Itinerario

class Usuario:
    def __init__(self, nombre: str, preferencias: list[str], presupuesto_maximo: float, itinerarios: List[Itinerario]):
        self.nombre: str = nombre
        self.preferencias: list[str] = preferencias
        self.presupuesto_maximo: float = presupuesto_maximo
        self.itinerarios: list[Itinerario] = itinerarios

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "preferencias": self.preferencias,
            "presupuesto_maximo": self.presupuesto_maximo,
            "itinerarios": [itinerario.to_dict() for itinerario in self.itinerarios]
        }

    def __str__(self) -> str:
        return f"Usuario: {self.nombre}, Preferencias: {', '.join(self.preferencias)}, Presupuesto: ${self.presupuesto_maximo}"

