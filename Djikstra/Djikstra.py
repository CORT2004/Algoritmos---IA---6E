# ============================================================
# ALGORITMO DE DIJKSTRA
#
# Ejemplo práctico:
# Encontrar la ruta más corta entre sucursales
# de una empresa de paquetería.
#
# Características:
# - Muestra cada actualización
# - Explicaciones detalladas
# ============================================================

import math


def mostrar_tabla(distancias, visitados):
    """
    Muestra el estado actual del algoritmo.
    """

    print("\nEstado actual:")

    print("-" * 40)

    print("Nodo\tDistancia\tVisitado")

    print("-" * 40)

    for nodo in distancias:

        print(
            f"{nodo}\t"
            f"{distancias[nodo]}\t\t"
            f"{visitados[nodo]}"
        )


def dijkstra(grafo, inicio):
    """
    Implementación paso a paso
    del algoritmo de Dijkstra.
    """

    # Distancias iniciales
    distancias = {}

    # Nodos visitados
    visitados = {}

    for nodo in grafo:

        distancias[nodo] = math.inf
        visitados[nodo] = False

    distancias[inicio] = 0

    print("\n================================")
    print("INICIANDO DIJKSTRA")
    print("================================")

    paso = 1

    for _ in range(len(grafo)):

        print("\n" + "=" * 50)
        print(f"PASO {paso}")
        print("=" * 50)

        # Buscar nodo no visitado
        # con menor distancia
        nodo_actual = None
        menor_distancia = math.inf

        for nodo in grafo:

            if (not visitados[nodo] and
                    distancias[nodo] < menor_distancia):

                menor_distancia = distancias[nodo]
                nodo_actual = nodo

        if nodo_actual is None:
            break

        print(
            f"\nNodo seleccionado: "
            f"{nodo_actual}"
        )

        print(
            f"Distancia acumulada: "
            f"{distancias[nodo_actual]}"
        )

        visitados[nodo_actual] = True

        # Revisar vecinos
        for vecino, peso in grafo[nodo_actual].items():

            if not visitados[vecino]:

                nueva_distancia = (
                    distancias[nodo_actual]
                    + peso
                )

                print(
                    f"\nEvaluando ruta:"
                )

                print(
                    f"{nodo_actual} -> "
                    f"{vecino}"
                )

                print(
                    f"Peso: {peso}"
                )

                print(
                    f"Distancia posible: "
                    f"{nueva_distancia}"
                )

                if nueva_distancia < distancias[vecino]:

                    print(
                        "¡Se encontró una "
                        "ruta más corta!"
                    )

                    distancias[vecino] = nueva_distancia

                else:

                    print(
                        "No mejora la ruta actual."
                    )

        mostrar_tabla(
            distancias,
            visitados
        )

        paso += 1

    return distancias


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("         ALGORITMO DE DIJKSTRA")
print("=" * 60)

print("\nEjemplo práctico:")
print("Encontrar la ruta más corta")
print("entre sucursales de una empresa.")

# ------------------------------------------------------------
# Captura de nodos
# ------------------------------------------------------------

cantidad_nodos = int(
    input("\n¿Cuántas sucursales existen?: ")
)

grafo = {}

for i in range(cantidad_nodos):

    nombre = input(
        f"Nombre de la sucursal #{i+1}: "
    ).upper()

    grafo[nombre] = {}

# ------------------------------------------------------------
# Captura de conexiones
# ------------------------------------------------------------

cantidad_conexiones = int(
    input(
        "\n¿Cuántas conexiones existen?: "
    )
)

for i in range(cantidad_conexiones):

    print(f"\nConexión #{i+1}")

    origen = input(
        "Sucursal origen: "
    ).upper()

    destino = input(
        "Sucursal destino: "
    ).upper()

    distancia = int(
        input(
            "Distancia entre ellas: "
        )
    )

    # Grafo no dirigido
    grafo[origen][destino] = distancia
    grafo[destino][origen] = distancia

# ------------------------------------------------------------
# Nodo inicial
# ------------------------------------------------------------

inicio = input(
    "\nSucursal de inicio: "
).upper()

resultado = dijkstra(
    grafo,
    inicio
)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

for nodo, distancia in resultado.items():

    print(
        f"Distancia mínima "
        f"hasta {nodo}: {distancia}"
    )