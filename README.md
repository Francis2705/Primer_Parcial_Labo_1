# Manejo de datos y archivos con Python (csv, json, txt)

Este proyecto consiste en un sistema de análisis y manipulación de datos de personajes, utilizando archivos en formatos csv, json y txt. Está implementado en Python y organizado en torno a un menú interactivo que permite ejecutar diversas funciones relacionadas con la lectura, transformación, análisis, guardado y visualización de información.

## 📂 Estructura del proyecto

- `primer_parcial_labo.py`: Script principal que muestra un menú para interactuar con los datos.
- `funciones_parcial.py`: Módulo que contiene todas las funciones necesarias para procesar los datos.

## 📌 Requisitos

- Python 3.10 o superior
- Módulos:
  - `re`
  - `datetime`
  - `json`
  - `unidecode`
  - `os`
  - `random`

Instalación rápida de dependencias:

```bash
pip install unidecode
```

## 🧠 Funcionalidades principales
✅ 1. Lectura de Datos
- Lectura y parseo de un archivo .csv llamado DBZ.csv.
- Conversión de campos como raza y habilidades en listas.
- Normalización de caracteres (acentos, símbolos).

📊 2. Análisis
- Contar cuántos personajes hay por raza o habilidad.
- Listar personajes por raza u otra característica.
- Calcular promedios entre atributos (poder_pelea, poder_ataque).
- Agrupar información en estructuras similares a JSON para análisis avanzados.

🥊 3. Simulación de Peleas
- Selección de personajes por nombre.
- Comparación de poder de ataque con otro personaje aleatorio.
- Registro del resultado en un archivo peleas.txt.

💾 4. Exportación de Datos
- Guardado de personajes filtrados en archivos .json.
- Generación de un nuevo archivo .csv con personajes modificados (poderes aumentados + nueva habilidad).

🔁 5. Modificación
- Incremento de poderes en base a características específicas (por ejemplo, raza = saiyan).
- Agregado de nuevas habilidades.

## 🗃️ Formatos de archivos utilizados
- `csv`: formato en el que se encuentran los datos originales de los personajes
- `json`: se utiliza para guardar personajes con filtros especificos
- `txt`: historial de peleas entre personajes, con fecha y resultado

## 👨‍💻 Ejecución
```bash
python primer_parcial_labo.py
```
