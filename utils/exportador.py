def exportar_itinerario(itinerario, formato='txt'):
    """Exporta un itinerario a archivo"""
    nombre_archivo = f"{itinerario.nombre.lower().replace(' ', '_')}.{formato}"
    contenido = f"Itinerario: {itinerario.nombre}\n\nActividades:\n"

    for i, act in enumerate(itinerario.actividades, 1):
        contenido += f"\n{i}. {act.nombre} ({act.categoria})\n"
        contenido += f"   Ubicación: {act.ubicacion}\n"
        contenido += f"   Costo: ${act.costo:.2f}\n"

    with open(nombre_archivo, 'w') as f:
        f.write(contenido)

    return nombre_archivo