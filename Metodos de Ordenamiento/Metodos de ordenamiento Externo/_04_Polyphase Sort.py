# ============================================================
# POLYPHASE SORT (SIMULACIÓN EDUCATIVA)
#
# Ejemplo práctico:
# Ordenar transacciones bancarias.
#
# El programa:
# - Genera corridas ordenadas.
# - Simula archivos temporales.
# - Muestra cada fase de mezcla.
# ============================================================


def crear_corridas(datos, tamaño_corrida):
    """
    Divide la lista en corridas ordenadas.
    """

    corridas = []

    print("\n================================")
    print("CREANDO CORRIDAS")
    print("================================")

    for i in range(0, len(datos), tamaño_corrida):

        corrida = datos[i:i + tamaño_corrida]

        print(f"\nBloque original: {corrida}")

        corrida.sort()

        print(f"Corrida ordenada: {corrida}")

        corridas.append(corrida)

    return corridas


def mezclar_corridas(corrida1, corrida2):
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

            resultado.append(corrida1[i])

            print(
                f"Se agrega {corrida1[i]}"
            )

            i += 1

        else:

            resultado.append(corrida2[j])

            print(
                f"Se agrega {corrida2[j]}"
            )

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

    print("Resultado:", resultado)

    return resultado


def polyphase_sort(datos, tamaño_corrida):
    """
    Simulación educativa del Polyphase Sort.
    """

    corridas = crear_corridas(
        datos,
        tamaño_corrida
    )

    print("\n================================")
    print("DISTRIBUCIÓN INICIAL")
    print("================================")

    archivo_a = []
    archivo_b = []

    for i, corrida in enumerate(corridas):

        if i % 2 == 0:
            archivo_a.append(corrida)
        else:
            archivo_b.append(corrida)

    print("\nArchivo A:")
    print(archivo_a)

    print("\nArchivo B:")
    print(archivo_b)

    fase = 1

    while len(corridas) > 1:

        print("\n" + "=" * 60)
        print(f"FASE {fase}")
        print("=" * 60)

        nuevas_corridas = []

        i = 0

        while i < len(corridas):

            if i + 1 < len(corridas):

                nueva = mezclar_corridas(
                    corridas[i],
                    corridas[i + 1]
                )

                nuevas_corridas.append(nueva)

            else:

                print(
                    "\nCorrida sin pareja:"
                )

                print(corridas[i])

                nuevas_corridas.append(corridas[i])

            i += 2

        corridas = nuevas_corridas

        print("\nCorridas después de la fase:")
        print(corridas)

        fase += 1

    return corridas[0]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("              POLYPHASE SORT")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar transacciones bancarias.")

cantidad = int(
    input("\n¿Cuántos registros desea ingresar?: ")
)

datos = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese el registro #{i+1}: ")
    )

    datos.append(numero)

tamaño_corrida = int(
    input(
        "\nTamaño de cada corrida inicial: "
    )
)

resultado = polyphase_sort(
    datos,
    tamaño_corrida
)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)