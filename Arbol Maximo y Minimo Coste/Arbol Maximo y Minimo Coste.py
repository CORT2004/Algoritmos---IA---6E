# ============================================================
# ÁRBOL DE MÍNIMO Y MÁXIMO COSTE
#
# Ejemplo práctico:
# Conectar ciudades mediante fibra óptica.
#
# Características:
# - Muestra todas las conexiones evaluadas
# - Permite calcular árbol mínimo o máximo
# ============================================================


def arbol_coste(grafo, inicio, tipo):

    visitados = {inicio}

    arbol = []

    costo_total = 0

    paso = 1

    print("\n" + "=" * 60)

    if tipo == "min":
        print("ÁRBOL DE MÍNIMO COSTE")
    else:
        print("ÁRBOL DE MÁXIMO COSTE")

    print("=" * 60)

    while len(visitados) < len(grafo):

        mejor_arista = None

        if tipo == "min":
            mejor_valor = float("inf")
        else:
            mejor_valor = float("-inf")

        print("\n" + "-" * 50)
        print(f"PASO {paso}")
        print("-" * 50)

        print("\nNodos conectados:")
        print(visitados)

        # Buscar la mejor conexión
        for origen in visitados:

            for destino, costo in grafo[origen].items():

                if destino not in visitados:

                    print(
                        f"Evaluando: "
                        f"{origen} -> {destino}"
                        f" (Costo {costo})"
                    )

                    if tipo == "min":

                        if costo < mejor_valor:

                            mejor_valor = costo

                            mejor_arista = (
                                origen,
                                destino,
                                costo
                            )

                    else:

                        if costo > mejor_valor:

                            mejor_valor = costo

                            mejor_arista = (
                                origen,
                                destino,
                                costo
                            )

        if mejor_arista is None:

            print(
                "\nEl grafo no está conectado."
            )

            return None

        origen, destino, costo = mejor_arista

        print(
            f"\nSe selecciona:"
        )

        print(
            f"{origen} -> {destino}"
        )

        print(
            f"Costo = {costo}"
        )

        visitados.add(destino)

        arbol.append(
            (origen, destino, costo)
        )

        costo_total += costo

        print(
            f"Costo acumulado: "
            f"{costo_total}"
        )

        paso += 1

    return arbol, costo_total


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("    ÁRBOL DE MÍNIMO Y MÁXIMO COSTE")
print("=" * 60)

print("\nEjemplo práctico:")
print("Conectar ciudades mediante fibra óptica.")

cantidad_nodos = int(
    input(
        "\n¿Cuántas ciudades existen?: "
    )
)

grafo = {}

for i in range(cantidad_nodos):

    ciudad = input(
        f"Ciudad #{i+1}: "
    ).upper()

    grafo[ciudad] = {}

cantidad_aristas = int(
    input(
        "\n¿Cuántas conexiones existen?: "
    )
)

for i in range(cantidad_aristas):

    print(f"\nConexión #{i+1}")

    origen = input(
        "Ciudad origen: "
    ).upper()

    destino = input(
        "Ciudad destino: "
    ).upper()

    costo = int(
        input(
            "Costo de conexión: "
        )
    )

    grafo[origen][destino] = costo
    grafo[destino][origen] = costo

inicio = input(
    "\nCiudad inicial: "
).upper()

tipo = input(
    "\n¿Desea árbol mínimo o máximo? "
    "(min/max): "
).lower()

resultado = arbol_coste(
    grafo,
    inicio,
    tipo
)

if resultado:

    arbol, costo_total = resultado

    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)

    print("\nConexiones seleccionadas:")

    for origen, destino, costo in arbol:

        print(
            f"{origen} -> {destino}"
            f" (Costo {costo})"
        )

    print(
        f"\nCosto total: "
        f"{costo_total}"
    )