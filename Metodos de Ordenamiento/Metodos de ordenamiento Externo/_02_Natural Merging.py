# ============================================================
# ALGORITMO NATURAL MERGING (MEZCLA NATURAL)
#
# Ejemplo práctico:
# Ordenar registros de ventas por número de operación.
#
# Características:
# - Detecta corridas naturales
# - Muestra cada mezcla realizada
# - Explica paso a paso el proceso
# ============================================================


def detectar_corridas(lista):
    """
    Detecta las corridas naturales existentes
    dentro de la lista.
    """

    corridas = []
    corrida_actual = [lista[0]]

    for i in range(1, len(lista)):

        # Si sigue ordenado, continúa la corrida
        if lista[i] >= lista[i - 1]:

            corrida_actual.append(lista[i])

        else:
            # Termina la corrida actual
            corridas.append(corrida_actual)

            corrida_actual = [lista[i]]

    corridas.append(corrida_actual)

    return corridas


def mezclar(corrida1, corrida2):
    """
    Mezcla dos corridas ordenadas.
    """

    print("\nMezclando:")
    print("Corrida 1:", corrida1)
    print("Corrida 2:", corrida2)

    resultado = []

    i = 0
    j = 0

    while i < len(corrida1) and j < len(corrida2):

        print(
            f"Comparando "
            f"{corrida1[i]} y {corrida2[j]}"
        )

        if corrida1[i] <= corrida2[j]:

            print(f"Se agrega {corrida1[i]}")

            resultado.append(corrida1[i])
            i += 1

        else:

            print(f"Se agrega {corrida2[j]}")

            resultado.append(corrida2[j])
            j += 1

    while i < len(corrida1):

        print(
            f"Agregando restante "
            f"{corrida1[i]}"
        )

        resultado.append(corrida1[i])
        i += 1

    while j < len(corrida2):

        print(
            f"Agregando restante "
            f"{corrida2[j]}"
        )

        resultado.append(corrida2[j])
        j += 1

    print("Resultado de la mezcla:", resultado)

    return resultado


def natural_merging(lista):
    """
    Implementación del método Natural Merging.
    """

    print("\n================================")
    print("INICIO DEL NATURAL MERGING")
    print("================================")

    print("\nLista original:")
    print(lista)

    pasada = 1

    while True:

        print("\n" + "=" * 60)
        print(f"PASADA {pasada}")
        print("=" * 60)

        # Detectar corridas naturales
        corridas = detectar_corridas(lista)

        print("\nCorridas encontradas:")

        for i, corrida in enumerate(corridas, start=1):
            print(f"Corrida {i}: {corrida}")

        # Si solo existe una corrida,
        # la lista ya está ordenada
        if len(corridas) == 1:

            print(
                "\nSolo existe una corrida."
            )

            print(
                "La lista ya está completamente ordenada."
            )

            return corridas[0]

        nuevas_corridas = []

        i = 0

        while i < len(corridas):

            if i + 1 < len(corridas):

                mezcla = mezclar(
                    corridas[i],
                    corridas[i + 1]
                )

                nuevas_corridas.append(mezcla)

            else:

                print(
                    "\nCorrida sin pareja:"
                )

                print(corridas[i])

                nuevas_corridas.append(corridas[i])

            i += 2

        # Reconstruir lista
        lista = []

        for corrida in nuevas_corridas:
            lista.extend(corrida)

        print("\nLista después de la pasada:")
        print(lista)

        pasada += 1


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("        ORDENAMIENTO NATURAL MERGING")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar registros de ventas.")

cantidad = int(
    input("\n¿Cuántos registros desea ingresar?: ")
)

datos = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese el registro #{i+1}: ")
    )

    datos.append(numero)

resultado = natural_merging(datos)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)