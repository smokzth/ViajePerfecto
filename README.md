# 🌍 Viaje Perfecto

![Diagrama de Clases](/docs/diagrama.jpg)

## Descripción

**"Viaje Perfecto"** es una aplicación de consola diseñada para ayudar a los usuarios a planificar viajes personalizados de manera sencilla. A través de una interfaz interactiva, los usuarios pueden registrarse, crear itinerarios y visualizar los planes creados. Este producto mínimo viable (PMV) se enfoca en sentar las bases para un sistema más completo y funcional a futuro.

---

## Estructura del Proyecto

La estructura del proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)** para mantener un código organizado, escalable y fácil de mantener.

### 📁 Carpetas

- **`controllers/`**: Lógica de control:
  - `controlador_principal.py`

- **`models/`**: Clases que representan el modelo de datos:
  - `usuario.py`: Datos del usuario.
  - `itinerario.py`: Planificación de viajes.
  - `actividad.py`: Actividades del itinerario (aún no usada).
  - `entrada_diario.py`: Entradas del diario de viaje (aún no usada).

- **`views/`**: Interfaz de consola:
  - `vista_consola.py`

- **`utils/`** *(aún sin uso en el PMV)*: Lugar para futuras funciones auxiliares como persistencia, mapas, y presupuesto.

- **`data/`**:
  - `usuarios.json`, `ubicacion.json`: Archivos JSON simulando persistencia.
  
- **`docs\`**:
-  `docs/diagrama.jpg`: Diagrama de clases (ver arriba).
- **Archivo raíz**:
  - `main.py`: Punto de entrada principal del programa.
  - `.gitignore`, `pyproject.toml`, `README.md`: Archivos de configuración y documentación.

---

## 📌 Archivos actuales

viaje_perfecto/ ├── controllers/ │ └── controlador_principal.py ├── data/ │ ├── usuarios.json │ ├── ubicacion.json │ └── docs/ │ └── diagrama.jpg ├── models/ │ ├── usuario.py │ ├── itinerario.py │ ├── actividad.py │ └── entrada_diario.py ├── utils/ ├── views/ │ └── vista_consola.py ├── main.py ├── .gitignore ├── pyproject.toml └── README.md


---

## ✅ Funcionalidades actuales

- Registro de usuario (nombre, preferencias, presupuesto).
- Creación de itinerarios asociados al usuario.
- Visualización de itinerarios por consola.

---

## 🔜 Funcionalidades futuras

- Agregar actividades al itinerario.
- Agregar entradas al diario de viaje.
- Recomendaciones inteligentes según preferencias.
- Mapa interactivo con optimización de rutas.
- Control de gastos y sugerencias personalizadas.
- Persistencia robusta de datos.

---

## ⚙️ Requisitos

- Python 3.10 o superior.
- Entorno de desarrollo: **PyCharm** recomendado.
- Por ahora, **no se requieren librerías externas**.

---

## ▶️ Cómo ejecutar

Desde la raíz del proyecto:

```bash
  python main.py
