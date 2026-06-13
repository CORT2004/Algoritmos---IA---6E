# ============================================================
# ALGORITMO DE PRIM
#
# Ejemplo práctico:
# Conectar ciudades mediante fibra óptica
# minimizando el costo total.
#
# Características:
# - Interactivo
# - Paso a paso
# - Explicación detallada
# - Muestra las conexiones seleccionadas
# ============================================================

def prim(grafo, inicio):

    # Nodos ya conectados al árbol
    visitados = set([inicio])

    # Aristas seleccionadas
    arbol_minimo = []

    # Costo total acumulado
    costo_total = 0

    paso = 1

    print("\n" + "=" * 60)
    print("INICIANDO ALGORITMO DE PRIM")
    print("=" * 60)

    while len(visitados) < len(grafo):

        print("\n" + "-" * 50)
        print(f"PASO {paso}")
        print("-" * 50)

        mejor_arista = None
        menor_costo = float('inf')

        print("\nNodos conectados actualmente:")
        print(visitados)

        # Buscar la arista más barata
        for nodo in visitados:

            for vecino, costo in grafo[nodo].items():

                if vecino not in visitados:

                    print(
                        f"Evaluando conexión "
                        f"{nodo} -> {vecino} "
                        f"(Costo: {costo})"
                    )

                    if costo < menor_costo:

                        menor_costo = costo
                        mejor_arista = (
                            nodo,
                            vecino,
                            costo
                        )

        if mejor_arista is None:
            print(
                "\nEl grafo no está conectado."
            )
            return None

        origen, destino, costo = mejor_arista

        print(
            f"\nSe selecciona la conexión:"
        )

        print(
            f"{origen} -> {destino}"
        )

        print(
            f"Costo: {costo}"
        )

        visitados.add(destino)

        arbol_minimo.append(
            (origen, destino, costo)
        )

        costo_total += costo

        print(
            f"\nCosto acumulado: "
            f"{costo_total}"
        )

        paso += 1

    return arbol_minimo, costo_total


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("     ÁRBOL MÍNIMO DE PRIM")
print("=" * 60)

print("\nEjemplo práctico:")
print("Conectar ciudades con fibra óptica")
print("al menor costo posible.")

# ------------------------------------------------------------
# INGRESO DE NODOS
# ------------------------------------------------------------

cantidad_nodos = int(
    input(
        "\n¿Cuántas ciudades existen?: "
    )
)

grafo = {}

for i in range(cantidad_nodos):

    ciudad = input(
        f"Nombre de la ciudad #{i+1}: "
    ).upper()

    grafo[ciudad] = {}

# ------------------------------------------------------------
# INGRESO DE CONEXIONES
# ------------------------------------------------------------

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

    # Grafo no dirigido
    grafo[origen][destino] = costo
    grafo[destino][origen] = costo

# ------------------------------------------------------------
# NODO INICIAL
# ------------------------------------------------------------

inicio = input(
    "\nCiudad inicial: "
).upper()

resultado = prim(grafo, inicio)

if resultado:

    arbol, costo_total = resultado

    print("\n" + "=" * 60)
    print("ÁRBOL DE EXPANSIÓN MÍNIMA")
    print("=" * 60)

    for origen, destino, costo in arbol:

        print(
            f"{origen} -> {destino}"
            f"  (Costo: {costo})"
        )

    print(
        f"\nCosto total mínimo: "
        f"{costo_total}"
    )