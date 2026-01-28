"""
Calculadora de promedios escolares.
Programa estructurado que permite ingresar materias y calificaciones,
calcular promedios, determinar aprobados/reprobados y encontrar extremos.
"""

UMBRAL_APROBACION = 5.0


def ingresar_calificaciones():
    """
    Permite al usuario introducir nombres de materias y calificaciones.
    Valida que las calificaciones estén entre 0 y 10.
    Retorna dos listas: una de nombres y otra de calificaciones.
    """
    materias = []
    calificaciones = []

    while True:
        # Solicitar nombre de la materia
        nombre_materia = input("\nIngrese el nombre de la materia: ").strip()
        if not nombre_materia:
            print("El nombre de la materia no puede estar vacío. Intente de nuevo.")
            continue

        # Solicitar y validar calificación
        while True:
            try:
                entrada = input("Ingrese la calificación (0-10): ").strip().replace(",", ".")
                nota = float(entrada)
                if 0 <= nota <= 10:
                    break
                print("La calificación debe estar entre 0 y 10. Intente de nuevo.")
            except ValueError:
                print("Debe ingresar un número válido. Intente de nuevo.")

        materias.append(nombre_materia)
        calificaciones.append(nota)

        # Preguntar si desea continuar
        while True:
            continuar = input("¿Desea agregar otra materia? (s/n): ").strip().lower()
            if continuar in ("s", "si", "sí", "n", "no"):
                break
            print("Responda 's' para sí o 'n' para no.")

        if continuar in ("n", "no"):
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Recibe una lista de calificaciones y devuelve el promedio.
    Retorna 0.0 si la lista está vacía.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Recibe la lista de calificaciones y un umbral.
    Retorna dos listas: índices de materias aprobadas e índices de reprobadas.
    """
    aprobados = []
    reprobados = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobados.append(i)
        else:
            reprobados.append(i)
    return aprobados, reprobados


def encontrar_extremos(calificaciones):
    """
    Identifica el índice de la calificación más alta y el de la más baja.
    Retorna (indice_max, indice_min). Si la lista está vacía, retorna (None, None).
    """
    if not calificaciones:
        return None, None
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min


def mostrar_resumen(materias, calificaciones, promedio, aprobados, reprobados,
                    indice_max, indice_min):
    """
    Muestra un resumen final con toda la información procesada.
    """
    print("\n" + "=" * 60)
    print("                    RESUMEN FINAL")
    print("=" * 60)

    print("\n--- Materias y calificaciones ---")
    for i in range(len(materias)):
        print(f"  • {materias[i]}: {calificaciones[i]:.2f}")

    print(f"\n--- Promedio general: {promedio:.2f} ---")

    if aprobados:
        print("\n--- Materias aprobadas ---")
        for idx in aprobados:
            print(f"  • {materias[idx]}: {calificaciones[idx]:.2f}")
    else:
        print("\n--- No hay materias aprobadas. ---")

    if reprobados:
        print("\n--- Materias reprobadas ---")
        for idx in reprobados:
            print(f"  • {materias[idx]}: {calificaciones[idx]:.2f}")
    else:
        print("\n--- No hay materias reprobadas. ---")

    if indice_max is not None:
        print(f"\n--- Mejor calificación: {materias[indice_max]} con {calificaciones[indice_max]:.2f} ---")
    if indice_min is not None:
        print(f"--- Peor calificación: {materias[indice_min]} con {calificaciones[indice_min]:.2f} ---")

    print("=" * 60)


def main():
    """Función principal que orquesta el flujo del programa."""
    print("\n=== CALCULADORA DE PROMEDIOS ESCOLARES ===")
    print("Ingrese materias y sus calificaciones (0-10).")
    print("Escriba 'n' cuando desee terminar de cargar datos.\n")

    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("\nNo se ingresó ninguna materia. No hay datos para procesar.")
        print("Hasta luego.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobados, reprobados = determinar_estado(calificaciones, UMBRAL_APROBACION)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    mostrar_resumen(materias, calificaciones, promedio, aprobados, reprobados,
                   indice_max, indice_min)

    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!\n")


if __name__ == "__main__":
    main()
