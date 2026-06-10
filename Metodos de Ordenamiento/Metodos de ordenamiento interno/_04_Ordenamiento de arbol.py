# ============================================================
# ORDENAMIENTO DE ÁRBOL (TREE SORT)
# Ejemplo práctico:
# Ordenar números de expediente de pacientes en un hospital
# ============================================================

# ------------------------------------------------------------
# Clase Nodo
# Cada nodo almacena:
# - Un dato
# - Un hijo izquierdo
# - Un hijo derecho
# ------------------------------------------------------------
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


# ------------------------------------------------------------
# Función para insertar valores en el árbol
# ------------------------------------------------------------
def insertar(nodo, valor):

    # Si el nodo está vacío, se crea uno nuevo
    if nodo is None:
        print(f"\nSe crea el nodo raíz con valor {valor}")
        return Nodo(valor)

    print(f"\nInsertando {valor}...")

    # Si el valor es menor, va a la izquierda
    if valor < nodo.valor:
        print(
            f"{valor} es menor que {nodo.valor} -> ir a la IZQUIERDA"
        )

        nodo.izquierda = insertar(nodo.izquierda, valor)

    # Si el valor es mayor o igual, va a la derecha
    else:
        print(
            f"{valor} es mayor o igual que {nodo.valor} -> ir a la DERECHA"
        )

        nodo.derecha = insertar(nodo.derecha, valor)

    return nodo


# ------------------------------------------------------------
# Recorrido In-Order
#
# Izquierda -> Raíz -> Derecha
#
# Este recorrido devuelve los elementos ordenados.
# ------------------------------------------------------------
def recorrido_inorden(nodo, lista_ordenada):

    if nodo is not None:

        # Visitar subárbol izquierdo
        recorrido_inorden(nodo.izquierda, lista_ordenada)

        print(
            f"Visitando nodo {nodo.valor} "
            f"y agregándolo a la lista ordenada"
        )

        lista_ordenada.append(nodo.valor)

        # Visitar subárbol derecho
        recorrido_inorden(nodo.derecha, lista_ordenada)


# ------------------------------------------------------------
# Mostrar estructura del árbol
# ------------------------------------------------------------
def mostrar_arbol(nodo, nivel=0):

    if nodo is not None:

        mostrar_arbol(nodo.derecha, nivel + 1)

        print("   " * nivel + str(nodo.valor))

        mostrar_arbol(nodo.izquierda, nivel + 1)


# ------------------------------------------------------------
# Función principal del Tree Sort
# ------------------------------------------------------------
def tree_sort(datos):

    raiz = None

    print("\n================================")
    print("CONSTRUCCIÓN DEL ÁRBOL")
    print("================================")

    # Insertar cada elemento en el árbol
    for numero in datos:
        raiz = insertar(raiz, numero)

    print("\n================================")
    print("ÁRBOL GENERADO")
    print("================================")
    mostrar_arbol(raiz)

    print("\n================================")
    print("RECORRIDO IN-ORDER")
    print("================================")

    lista_ordenada = []

    recorrido_inorden(raiz, lista_ordenada)

    return lista_ordenada


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("===========================================")
print("      ORDENAMIENTO DE ÁRBOL (TREE SORT)")
print("===========================================")

print("\nEjemplo práctico:")
print("Ordenar expedientes de pacientes de un hospital.")

cantidad = int(
    input("\n¿Cuántos expedientes desea ingresar?: ")
)

datos = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese el expediente #{i+1}: ")
    )

    datos.append(numero)

print("\nLista ingresada:")
print(datos)

resultado = tree_sort(datos)

print("\n================================")
print("RESULTADO FINAL")
print("================================")
print("Lista ordenada:")
print(resultado)