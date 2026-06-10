# ============================================================
# ALGORITMO STRAIGHT MERGING (MEZCLA DIRECTA)
#
# Ejemplo práctico:
# Ordenar matrículas de estudiantes
#
# Características:
# - Muestra cada pasada
# - Muestra cada mezcla realizada
# - Explica paso a paso el proceso
# ============================================================


def mezclar(bloque1, bloque2):
    """
    Mezcla dos bloques ordenados
    y devuelve un único bloque ordenado.
    """

    resultado = []

    i = 0
    j = 0

    print("\nMezclando:")
    print("Bloque 1:", bloque1)
    print("Bloque 2:", bloque2)

    while i < len(bloque1) and j < len(bloque2):

        print(
            f"Comparando {bloque1[i]} y {bloque2[j]}"
        )

        if bloque1[i] <= bloque2[j]:

            print(f"Se agrega {bloque1[i]}")

            resultado.append(bloque1[i])
            i += 1

        else:

            print(f"Se agrega {bloque2[j]}")

            resultado.append(bloque2[j])
            j += 1

    # Agregar elementos restantes
    while i < len(bloque1):

        print(
            f"Agregando restante {bloque1[i]}"
        )

        resultado.append(bloque1[i])
        i += 1

    while j < len(bloque2):

        print(
            f"Agregando restante {bloque2[j]}"
        )

        resultado.append(bloque2[j])
        j += 1

    print("Resultado de la mezcla:", resultado)

    return resultado


def straight_merging(lista):
    """
    Implementación iterativa de Straight Merging.
    """

    n = len(lista)

    print("\n================================")
    print("INICIO DEL STRAIGHT MERGING")
    print("================================")

    print("\nLista original:")
    print(lista)

    # --------------------------------------------------------
    # PASO 1:
    # Convertir cada elemento en un bloque individual.
    # --------------------------------------------------------

    bloques = [[elemento] for elemento in lista]

    print("\nBloques iniciales:")
    print(bloques)

    pasada = 1

    # --------------------------------------------------------
    # Continuar mientras exista más de un bloque
    # --------------------------------------------------------

    while len(bloques) > 1:

        print("\n" + "=" * 60)
        print(f"PASADA {pasada}")
        print("=" * 60)

        nuevos_bloques = []

        i = 0

        while i < len(bloques):

            # Si existe un par de bloques
            if i + 1 < len(bloques):

                mezcla = mezclar(
                    bloques[i],
                    bloques[i + 1]
                )

                nuevos_bloques.append(mezcla)

            else:
                # Si queda un bloque sin pareja
                print(
                    "\nBloque sin pareja, pasa directamente:"
                )

                print(bloques[i])

                nuevos_bloques.append(bloques[i])

            i += 2

        bloques = nuevos_bloques

        print("\nBloques después de la pasada:")
        print(bloques)

        pasada += 1

    return bloques[0]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("      ORDENAMIENTO STRAIGHT MERGING")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar matrículas de estudiantes.")

cantidad = int(
    input("\n¿Cuántas matrículas desea ingresar?: ")
)

matriculas = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese la matrícula #{i+1}: ")
    )

    matriculas.append(numero)

resultado = straight_merging(matriculas)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)