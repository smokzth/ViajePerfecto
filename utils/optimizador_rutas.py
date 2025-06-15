from math import radians, sin, cos, sqrt, atan2


def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula distancia entre dos coordenadas (Haversine)"""
    R = 6371  # Radio de la Tierra en km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def optimizar_ruta(actividades):
    """Ordena actividades por proximidad geográfica"""
    if not actividades:
        return []

    ordenadas = [actividades[0]]
    restantes = actividades[1:]

    while restantes:
        ultima = ordenadas[-1]
        mas_cercana = min(
            restantes,
            key=lambda x: calcular_distancia(
                ultima.latitud, ultima.longitud,
                x.latitud, x.longitud
            )
        )
        ordenadas.append(mas_cercana)
        restantes.remove(mas_cercana)

    return ordenadas