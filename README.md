# Trabajo 1 – Sintaxis de Python

Tarea 1: sintaxis de Python. Desarrollo de una **calculadora de promedios escolares** usando variables, operadores, estructuras de control y funciones básicas (programación estructurada, sin POO).

---

## ¿Qué se hizo?

Se creó el programa **`calculadora_promedios.py`**, que permite:

- Ingresar nombres de materias y sus calificaciones (valores entre 0 y 10).
- Almacenar todo en listas (una para materias, otra para calificaciones).
- Calcular y mostrar el promedio general.
- Determinar materias aprobadas y reprobadas según el umbral 5.0.
- Mostrar la materia con mejor y peor calificación.
- Añadir tantas materias como se quiera y finalizar cuando el usuario lo indique.
- Mostrar un resumen final con toda la información.

---

## Estructura del programa

| Función | Descripción |
|--------|-------------|
| `ingresar_calificaciones()` | Pide nombre de materia y calificación (validada 0–10), pregunta si seguir y devuelve las dos listas. |
| `calcular_promedio(calificaciones)` | Recibe la lista de calificaciones y devuelve el promedio. |
| `determinar_estado(calificaciones, umbral)` | Devuelve listas de índices de aprobados y reprobados (umbral por defecto 5.0). |
| `encontrar_extremos(calificaciones)` | Devuelve el índice de la nota más alta y el de la más baja. |
| `mostrar_resumen(...)` | Imprime el resumen: materias, promedio, aprobadas/reprobadas y extremos. |
| `main()` | Orquesta el flujo: ingresar datos, calcular y mostrar el resumen. |

- Validación de entradas: calificaciones numéricas entre 0 y 10, nombres no vacíos.
- Caso sin materias: si no se ingresa ninguna, se informa y se sale sin error.

---

## Cómo ejecutarlo

Requisitos: Python 3.

```bash
python3 calculadora_promedios.py
```

Durante la ejecución se pide:

1. Nombre de la materia.
2. Calificación (0–10).
3. Si se desea agregar otra materia (`s`/`n`).

Al terminar de cargar, se muestra el resumen con promedios, aprobados/reprobados y mejor/peor calificación.

---

## Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `calculadora_promedios.py` | Programa completo de la calculadora de promedios. |
| `calculadora.py` | Vacío / reservado para otro uso. |
| `README.md` | Este archivo. |
