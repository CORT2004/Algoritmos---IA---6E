# ============================================================
# ALGORITMO QUICK SORT
# Ejemplo práctico:
# Ordenar precios de productos de una tienda en línea
#
# El programa:
# 2. Muestra paso a paso cómo trabaja Quick Sort.
# 3. Explica la selección del pivote.
# 4. Muestra las particiones realizadas.
# ============================================================


def quick_sort(lista, nivel=0):
    """
    Función recursiva Quick Sort.

    Parámetros:
    lista -> Lista a ordenar.
    nivel -> Nivel de profundidad de la recursión
             (solo para mejorar la visualización).
    """

    sangria = "   " * nivel

    print(f"\n{sangria}Trabajando con: {lista}")

    # Caso base:
    # Si la lista tiene 0 o 1 elemento ya está ordenada.
    if len(lista) <= 1:
        print(f"{sangria}La lista ya está ordenada: {lista}")
        return lista

    # --------------------------------------------------------
    # Selección del pivote
    # En este ejemplo utilizamos el último elemento.
    # --------------------------------------------------------
    pivote = lista[-1]

    print(f"{sangria}Pivote seleccionado: {pivote}")

    menores = []
    iguales = []
    mayores = []

    # --------------------------------------------------------
    # División de elementos
    # --------------------------------------------------------
    for elemento in lista:

        if elemento < pivote:
            menores.append(elemento)

        elif elemento == pivote:
            iguales.append(elemento)

        else:
            mayores.append(elemento)

    print(f"{sangria}Menores que el pivote: {menores}")
    print(f"{sangria}Iguales al pivote: {iguales}")
    print(f"{sangria}Mayores que el pivote: {mayores}")

    # --------------------------------------------------------
    # Llamadas recursivas
    # --------------------------------------------------------
    print(f"{sangria}Ordenando sublista izquierda...")
    izquierda = quick_sort(menores, nivel + 1)

    print(f"{sangria}Ordenando sublista derecha...")
    derecha = quick_sort(mayores, nivel + 1)

    # --------------------------------------------------------
    # Combinar resultados
    # --------------------------------------------------------
    resultado = izquierda + iguales + derecha

    print(f"{sangria}Resultado combinado: {resultado}")

    return resultado


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("        ORDENAMIENTO QUICK SORT")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar precios de productos de una tienda en línea.")

cantidad = int(
    input("\n¿Cuántos precios desea ingresar?: ")
)

precios = []

for i in range(cantidad):

    precio = float(
        input(f"Ingrese el precio #{i + 1}: ")
    )

    precios.append(precio)

print("\nLista original:")
print(precios)

print("\n" + "=" * 60)
print("INICIANDO QUICK SORT")
print("=" * 60)

resultado = quick_sort(precios)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)