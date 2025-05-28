# Sistema de Registro y Reporte de Talleres Culturales Comunitarios

Este proyecto consiste en el desarrollo de una aplicación de escritorio destinada a una casa de la cultura, con el objetivo de facilitar el registro, la gestión y el análisis de la participación en talleres culturales comunitarios como pintura, teatro, música y danza. 

El sistema permite registrar participantes, gestionar sus asistencias, calcular pagos conforme al tipo de taller y generar reportes analíticos con visualizaciones estadísticas. Está desarrollado en Python, aplicando principios de Programación Orientada a Objetos (POO), y cuenta con una interfaz gráfica intuitiva creada con Tkinter.

## Características

- Registro de participantes: nombre, edad, taller inscrito, mes y número de clases asistidas.
- Gestión de datos: modificación y eliminación de registros.
- Cálculo automático del valor pagado por cada participante según el taller.
- Análisis de datos con Pandas y visualización de resultados con Matplotlib.
- Interfaz gráfica organizada con `grid()` y separación lógica de funcionalidades.
- Control de versiones con Git y organización del repositorio en módulos.

## Talleres y valores por clase

| Taller   | Valor por clase |
|----------|-----------------|
| Pintura  | $6.000          |
| Teatro   | $8.000          |
| Música   | $10.000         |
| Danza    | $7.000          |

## Requisitos del sistema

- Python 3.11 o superior
- Pandas >= 1.5
- Matplotlib >= 3.5

Puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Estructura del repositorio

```
cultura_app/
├── app/
│   ├── interfaz.py         # Interfaz gráfica con Tkinter
│   ├── logica.py           # Clases y lógica del sistema
│   ├── analisis.py         # Análisis y visualización con Pandas y Matplotlib
│   └── datos/
│       └── participantes.csv  # Archivo de almacenamiento de datos
├── README.md               # Este archivo
├── requirements.txt        # Dependencias del proyecto
└── .gitignore              # Archivos ignorados por Git
```

## Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/Sxg0673/cultura_app.git
```

2. Activa el entorno virtual:

```bash
conda activate cultura_app
```

3. Ejecuta el archivo de la interfaz:

```bash
cd cultura_app
python -m app.interfaz
```
