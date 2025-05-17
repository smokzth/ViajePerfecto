import json
from models.usuario import Usuario
from models.itinerario import Itinerario
from models.actividad import Actividad
from models.entrada_diario import EntradaDiario

def cargar_usuarios():
    try:
        with open("data/usuarios.json", "r") as file:
            usuarios_data = json.load(file)
            usuarios = []
            for user_data in usuarios_data:
                # Convertir itinerarios de dict a objetos Itinerario
                itinerarios = []
                for itin_data in user_data.get('itinerarios', []):
                    # Convertir actividades de dict a objetos Actividad
                    actividades = [Actividad(**act) for act in itin_data.get('actividades', [])]
                    # Convertir entradas de diario de dict a objetos EntradaDiario
                    diario = [EntradaDiario(**entrada) for entrada in itin_data.get('diario', [])]
                    itinerario = Itinerario(
                        nombre=itin_data['nombre'],
                        usuario=user_data['nombre'],
                        actividades=actividades,
                        diario=diario
                    )
                    itinerarios.append(itinerario)

                usuario = Usuario(
                    nombre=user_data['nombre'],
                    preferencias=user_data['preferencias'],
                    presupuesto_maximo=user_data['presupuesto_maximo'],
                    itinerarios=itinerarios
                )
                usuarios.append(usuario)
            return usuarios
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Archivo JSON corrupto.")
        return []

def guardar_usuario(usuario: Usuario):
    usuarios = cargar_usuarios()
    # Evitar duplicados
    usuarios = [u for u in usuarios if u.nombre != usuario.nombre]
    usuarios.append(usuario)
    with open("data/usuarios.json", "w") as file:
        json.dump([u.to_dict() for u in usuarios], file, indent=4)

def eliminar_usuario(nombre: str):
    usuarios = [u for u in cargar_usuarios() if u.nombre != nombre]
    with open("data/usuarios.json", "w") as file:
        json.dump([u.to_dict() for u in usuarios], file, indent=4)