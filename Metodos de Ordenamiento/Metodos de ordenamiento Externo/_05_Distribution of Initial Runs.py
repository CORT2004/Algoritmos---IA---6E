# ============================================================
# DISTRIBUTION OF INITIAL RUNS
#
# Simulación educativa de la fase utilizada en
# algoritmos de ordenamiento externo.
#
# Ejemplo práctico:
# Organización de registros de envíos.
# ============================================================


def distribuir_corridas(datos,
                         tamaño_corrida,
                         cantidad_archivos):

    print("\n================================")
    print("GENERANDO CORRIDAS INICIALES")
    print("================================")

    corridas = []

    numero_corrida = 1

    # --------------------------------------------------------
    # Crear corridas
    # --------------------------------------------------------
    for i in range(0,
                   len(datos),
                   tamaño_corrida):

        bloque = datos[i:i + tamaño_corrida]

        print(f"\nCorrida {numero_corrida}")
        print("Bloque original:", bloque)

        bloque.sort()

        print("Bloque ordenado:", bloque)

        corridas.append(bloque)

        numero_corrida += 1

    # --------------------------------------------------------
    # Crear archivos simulados
    # --------------------------------------------------------
    archivos = []

    for _ in range(cantidad_archivos):
        archivos.append([])

    print("\n================================")
    print("DISTRIBUYENDO CORRIDAS")
    print("================================")

    # --------------------------------------------------------
    # Distribución circular (Round Robin)
    # --------------------------------------------------------
    archivo_actual = 0

    for i, corrida in enumerate(corridas):

        print(
            f"\nCorrida {i+1} -> "
            f"Archivo {archivo_actual + 1}"
        )

        archivos[archivo_actual].append(corrida)

        archivo_actual += 1

        if archivo_actual >= cantidad_archivos:
            archivo_actual = 0

    return archivos


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("      DISTRIBUTION OF INITIAL RUNS")
print("=" * 60)

print("\nEjemplo práctico:")
print("Distribuir registros de envíos en archivos temporales.")

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
        "\nTamaño de cada corrida: "
    )
)

cantidad_archivos = int(
    input(
        "Cantidad de archivos temporales: "
    )
)

archivos = distribuir_corridas(
    datos,
    tamaño_corrida,
    cantidad_archivos
)

print("\n" + "=" * 60)
print("RESULTADO DE LA DISTRIBUCIÓN")
print("=" * 60)

for i, archivo in enumerate(archivos):

    print(f"\nArchivo {i+1}")

    for corrida in archivo:
        print(corrida)