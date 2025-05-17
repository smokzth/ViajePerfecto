from typing import List
from models.actividad import Actividad
from models.entrada_diario import EntradaDiario

class Itinerario:
    def __init__(self, nombre: str, usuario: str, actividades: list[Actividad], diario: list[EntradaDiario]):
        self.nombre: str = nombre
        self.usuario: str = usuario
        self.actividades: List[Actividad] = actividades
        self.diario: List[EntradaDiario] = diario if diario is not None else []


    def agregar_actividad(self, actividad: Actividad) -> None:
        self.actividades.append(actividad)

    def agregar_entrada_diario(self, entrada: EntradaDiario) -> None:
        self.diario.append(entrada)

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "usuario": self.usuario,
            "actividades": [actividad.to_dict() for actividad in self.actividades],
            "diario": [entrada.to_dict() for entrada in self.diario]
        }

    def __str__(self) -> str:
        return (f"Itinerario: {self.nombre}\n"
                f" para {self.usuario}\n"
                f" | Actividades: {len(self.actividades)}\n"
                f" | Entradas en Diario: {len(self.diario)}")