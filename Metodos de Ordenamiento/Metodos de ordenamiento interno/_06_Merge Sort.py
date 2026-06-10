# ============================================================
# ALGORITMO MERGE SORT
# Ejemplo práctico:
# Ordenar códigos de libros de una biblioteca digital
#
# El programa:
# 2. Muestra paso a paso cómo se divide la lista.
# 3. Muestra el proceso de combinación (Merge).
# 4. Explica cada comparación realizada.
# ============================================================

def merge_sort(lista, nivel=0):
    """
    Función Merge Sort recursiva.
    
    Parámetros:
    lista -> lista a ordenar
    nivel -> profundidad de la recursión
             (para mostrar mejor la salida)
    """

    sangria = "   " * nivel

    print(f"\n{sangria}Trabajando con la lista: {lista}")

    # Caso base
    if len(lista) <= 1:
        print(f"{sangria}La lista ya está ordenada.")
        return lista

    # --------------------------------------------------------
    # DIVIDIR
    # --------------------------------------------------------
    mitad = len(lista) // 2

    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    print(f"{sangria}Dividiendo en:")
    print(f"{sangria}Izquierda: {izquierda}")
    print(f"{sangria}Derecha: {derecha}")

    # Llamadas recursivas
    izquierda = merge_sort(izquierda, nivel + 1)
    derecha = merge_sort(derecha, nivel + 1)

    # --------------------------------------------------------
    # COMBINAR (MERGE)
    # --------------------------------------------------------
    print(f"\n{sangria}Combinando:")
    print(f"{sangria}{izquierda} y {derecha}")

    resultado = []

    i = 0
    j = 0

    # Comparar elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):

        print(
            f"{sangria}Comparando "
            f"{izquierda[i]} y {derecha[j]}"
        )

        if izquierda[i] <= derecha[j]:

            resultado.append(izquierda[i])

            print(
                f"{sangria}Se agrega "
                f"{izquierda[i]}"
            )

            i += 1

        else:

            resultado.append(derecha[j])

            print(
                f"{sangria}Se agrega "
                f"{derecha[j]}"
            )

            j += 1

    # Agregar elementos restantes de izquierda
    while i < len(izquierda):

        resultado.append(izquierda[i])

        print(
            f"{sangria}Agregando restante "
            f"{izquierda[i]}"
        )

        i += 1

    # Agregar elementos restantes de derecha
    while j < len(derecha):

        resultado.append(derecha[j])

        print(
            f"{sangria}Agregando restante "
            f"{derecha[j]}"
        )

        j += 1

    print(f"{sangria}Resultado parcial: {resultado}")

    return resultado


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("           ORDENAMIENTO MERGE SORT")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar códigos de libros de una biblioteca.")

cantidad = int(
    input("\n¿Cuántos códigos desea ingresar?: ")
)

codigos = []

for i in range(cantidad):

    codigo = int(
        input(f"Ingrese el código #{i+1}: ")
    )

    codigos.append(codigo)

print("\nLista original:")
print(codigos)

print("\n" + "=" * 60)
print("INICIANDO MERGE SORT")
print("=" * 60)

resultado = merge_sort(codigos)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)