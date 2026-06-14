# ============================================================
# KRUSKAL - ÁRBOL MÍNIMO Y MÁXIMO COSTE
#
# Ejemplo práctico:
# Conectar ciudades mediante fibra óptica.
#
# Características:
# - Explica cada decisión
# - Detecta ciclos
# - Permite árbol mínimo o máximo
# ============================================================


# ------------------------------------------------------------
# ESTRUCTURA UNION-FIND
# Sirve para detectar ciclos
# ------------------------------------------------------------

class UnionFind:

    def __init__(self, nodos):

        self.padre = {}

        for nodo in nodos:
            self.padre[nodo] = nodo

    def buscar(self, nodo):

        if self.padre[nodo] != nodo:

            self.padre[nodo] = self.buscar(
                self.padre[nodo]
            )

        return self.padre[nodo]

    def unir(self, nodo1, nodo2):

        raiz1 = self.buscar(nodo1)
        raiz2 = self.buscar(nodo2)

        if raiz1 != raiz2:

            self.padre[raiz2] = raiz1

            return True

        return False


# ------------------------------------------------------------
# ALGORITMO KRUSKAL
# ------------------------------------------------------------

def kruskal(nodos, aristas, tipo):

    print("\n" + "=" * 60)

    if tipo == "min":
        print("KRUSKAL - ÁRBOL DE MÍNIMO COSTE")
    else:
        print("KRUSKAL - ÁRBOL DE MÁXIMO COSTE")

    print("=" * 60)

    # --------------------------------------------------------
    # Ordenar aristas
    # --------------------------------------------------------

    if tipo == "min":

        aristas.sort(key=lambda x: x[2])

    else:

        aristas.sort(
            key=lambda x: x[2],
            reverse=True
        )

    print("\nAristas ordenadas:")

    for origen, destino, costo in aristas:

        print(
            f"{origen} - {destino}"
            f" = {costo}"
        )

    uf = UnionFind(nodos)

    arbol = []

    costo_total = 0

    paso = 1

    # --------------------------------------------------------
    # Recorrer aristas ordenadas
    # --------------------------------------------------------

    for origen, destino, costo in aristas:

        print("\n" + "-" * 50)
        print(f"PASO {paso}")
        print("-" * 50)

        print(
            f"Evaluando: "
            f"{origen} - {destino}"
            f" (Costo {costo})"
        )

        raiz_origen = uf.buscar(origen)
        raiz_destino = uf.buscar(destino)

        print(
            f"Raíz de {origen}: "
            f"{raiz_origen}"
        )

        print(
            f"Raíz de {destino}: "
            f"{raiz_destino}"
        )

        # Si las raíces son diferentes
        # NO existe ciclo
        if uf.unir(origen, destino):

            print(
                "✔ Se agrega al árbol"
            )

            arbol.append(
                (origen, destino, costo)
            )

            costo_total += costo

        else:

            print(
                "✘ Se descarta "
                "(formaría un ciclo)"
            )

        paso += 1

        # Árbol completo
        if len(arbol) == len(nodos) - 1:
            break

    return arbol, costo_total


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("      KRUSKAL - MÍNIMO Y MÁXIMO COSTE")
print("=" * 60)

print("\nEjemplo práctico:")
print("Conectar ciudades mediante fibra óptica.")

# ------------------------------------------------------------
# INGRESO DE NODOS
# ------------------------------------------------------------

cantidad_nodos = int(
    input(
        "\n¿Cuántas ciudades existen?: "
    )
)

nodos = []

for i in range(cantidad_nodos):

    ciudad = input(
        f"Ciudad #{i+1}: "
    ).upper()

    nodos.append(ciudad)

# ------------------------------------------------------------
# INGRESO DE ARISTAS
# ------------------------------------------------------------

cantidad_aristas = int(
    input(
        "\n¿Cuántas conexiones existen?: "
    )
)

aristas = []

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

    aristas.append(
        (origen, destino, costo)
    )

# ------------------------------------------------------------
# TIPO DE ÁRBOL
# ------------------------------------------------------------

tipo = input(
    "\n¿Desea árbol mínimo o máximo? "
    "(min/max): "
).lower()

arbol, costo_total = kruskal(
    nodos,
    aristas,
    tipo
)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("\nAristas seleccionadas:")

for origen, destino, costo in arbol:

    print(
        f"{origen} - {destino}"
        f" = {costo}"
    )

print(
    f"\nCosto total: "
    f"{costo_total}"
)