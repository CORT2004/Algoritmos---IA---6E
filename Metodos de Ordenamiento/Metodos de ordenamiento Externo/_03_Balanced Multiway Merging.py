# ============================================================
# BALANCED MULTIWAY MERGING (3-WAY MERGE)
#
# Ejemplo práctico:
# Ordenar números de ventas provenientes
# de varios departamentos de una empresa.
#
# Características:
# - Muestra la creación de bloques
# - Muestra cada comparación
# - Simula una mezcla multicamino
# ============================================================


def dividir_en_bloques(lista, cantidad_bloques):
    """
    Divide la lista en varios bloques.
    """

    bloques = []

    tamaño = len(lista) // cantidad_bloques

    inicio = 0

    for i in range(cantidad_bloques - 1):

        bloques.append(
            sorted(lista[inicio:inicio + tamaño])
        )

        inicio += tamaño

    bloques.append(sorted(lista[inicio:]))

    return bloques


def multiway_merge(bloques):
    """
    Mezcla múltiples bloques ordenados.
    """

    print("\n================================")
    print("INICIANDO MEZCLA MULTICAMINO")
    print("================================")

    resultado = []

    # Índice actual de cada bloque
    indices = [0] * len(bloques)

    paso = 1

    while True:

        print("\n" + "-" * 50)
        print(f"Paso {paso}")
        print("-" * 50)

        candidatos = []

        # Buscar elemento disponible
        # de cada bloque
        for i in range(len(bloques)):

            if indices[i] < len(bloques[i]):

                valor = bloques[i][indices[i]]

                candidatos.append((valor, i))

                print(
                    f"Bloque {i+1} aporta: {valor}"
                )

        # Si ya no quedan elementos
        if not candidatos:
            break

        # Elegir el menor
        menor, bloque_origen = min(candidatos)

        print(
            f"Se selecciona el menor: {menor}"
        )

        resultado.append(menor)

        indices[bloque_origen] += 1

        print("Resultado parcial:")
        print(resultado)

        paso += 1

    return resultado


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("     BALANCED MULTIWAY MERGING")
print("=" * 60)

print("\nEjemplo práctico:")
print("Combinar registros de ventas")
print("provenientes de varios departamentos.")

cantidad = int(
    input("\n¿Cuántos datos desea ingresar?: ")
)

datos = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese el dato #{i+1}: ")
    )

    datos.append(numero)

cantidad_bloques = int(
    input(
        "\n¿En cuántos bloques desea dividir la información? "
        "(Ejemplo: 3): "
    )
)

if cantidad_bloques < 2:
    cantidad_bloques = 2

print("\nLista original:")
print(datos)

bloques = dividir_en_bloques(
    datos,
    cantidad_bloques
)

print("\n================================")
print("BLOQUES GENERADOS")
print("================================")

for i, bloque in enumerate(bloques):

    print(f"Bloque {i+1}: {bloque}")

resultado = multiway_merge(bloques)

print("\n================================")
print("RESULTADO FINAL")
print("================================")

print("Lista ordenada:")
print(resultado)