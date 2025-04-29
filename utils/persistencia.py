import json
import os

RUTA_USUARIOS = "data/usuarios.json"

def guardar_usuario(usuario):
    usuarios = cargar_usuarios()
    usuarios.append(usuario.to_dict())
    with open(RUTA_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def cargar_usuarios():
    if not os.path.exists(RUTA_USUARIOS):
        return []
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)


