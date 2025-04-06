# Viaje Perfecto

## Descripción

**"Viaje Perfecto"** es una aplicación de planificación de viajes personalizados diseñada para empoderar a los usuarios en la creación de itinerarios detallados y adaptados a sus preferencias, presupuesto y tiempo disponible. La aplicación ofrece funcionalidades innovadoras como la gestión inteligente del presupuesto, optimización de rutas mediante un mapa interactivo y la creación de un diario de viaje digital. Los usuarios pueden crear perfiles, seleccionar actividades, visualizar itinerarios, gestionar gastos y compartir sus experiencias de viaje.

## Estructura del Proyecto

La estructura del proyecto sigue una organización modular y escalable, con carpetas específicas para modelos, vistas, controladores, utilidades y datos. A continuación se detalla la función de cada carpeta y archivo:

### Carpetas

- **`viaje_perfecto/`**: Carpeta principal del proyecto, que contiene todos los módulos y archivos de la aplicación.
- **`models/`**: Contiene las definiciones de las clases que representan los modelos de datos del sistema (`Usuario`, `Actividad`, `Itinerario`, `Ubicacion`, `EntradaDiario`). Estas clases definen la estructura de los datos y las relaciones entre ellos.
- **`views/`**: Contiene la lógica de la interfaz de usuario, en este caso, la clase `VistaConsola` para la interacción a través de la terminal.
- **`controllers/`**: Contiene la lógica de control de la aplicación, gestionando las interacciones entre los modelos y las vistas. Aquí se implementa la clase `ControladorPrincipal`.
- **`utils/`**: Contiene módulos con funcionalidades auxiliares, como:
  - `persistencia.py`: para la persistencia de datos.
  - `presupuesto.py`: para la gestión de presupuestos.
  - `mapa.py`: para el cálculo de distancias y optimización de rutas.
  - `diario.py`: para la gestión del diario de viaje.
- **`data/`**: Contiene archivos de datos estáticos, como los archivos JSON para usuarios y actividades.

### Archivos

- **`viaje_perfecto/__init__.py`**: Archivo que convierte la carpeta `viaje_perfecto` en un módulo de Python. Permite importar submódulos desde esta carpeta.
- **`viaje_perfecto/main.py`**: Archivo que contiene el código para ejecutar la aplicación.
- **`README.md`**: Este archivo. Proporciona una descripción general del proyecto, su estructura y su propósito.
- **`.gitignore`**: Archivo que especifica qué archivos o carpetas deben ser ignorados por Git. Suele incluir archivos de configuración local, bases de datos temporales, y otros archivos que no deberían ser versionados.

## Funcionalidades Principales

- ✅ Creación y gestión de perfiles de usuario.
- 🔍 Búsqueda y filtrado de actividades turísticas.
- 📝 Creación y edición de itinerarios personalizados.
- 💰 Gestión inteligente del presupuesto con alertas y sugerencias.
- 🗺️ Visualización de actividades en un mapa interactivo y optimización de rutas.
- 📓 Creación y gestión de un diario de viaje digital.
- 📤 Compartición y exportación de itinerarios y diarios de viaje.

## Dependencias

- `folium` *(opcional, si se utiliza para mapas)*
