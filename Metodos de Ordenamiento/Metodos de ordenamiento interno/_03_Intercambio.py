# ============================================================
# ALGORITMO DE ORDENAMIENTO POR INTERCAMBIO (EXCHANGE SORT)
# Ejemplo práctico:
# Ordenar los precios de productos de una tienda
# ============================================================

def intercambio_paso_a_paso(lista):
    """
    Función que ordena una lista utilizando el método
    de intercambio (Exchange Sort) y muestra cada paso.
    """

    n = len(lista)

    print("\n==============================")
    print("INICIO DEL ORDENAMIENTO")
    print("==============================")
    print("Lista inicial:", lista)

    # Recorremos cada posición de la lista
    for i in range(n - 1):

        print(f"\n--- PASADA {i + 1} ---")

        # Comparamos el elemento actual con todos los siguientes
        for j in range(i + 1, n):

            print(
                f"Comparando posición {i} ({lista[i]}) "
                f"con posición {j} ({lista[j]})"
            )

            # Si el elemento actual es mayor, intercambiamos
            if lista[i] > lista[j]:

                print(
                    f"→ {lista[i]} es mayor que {lista[j]}"
                )
                print("→ Se realiza un intercambio")

                # Intercambio de valores
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

                print("Lista después del intercambio:")
                print(lista)

            else:
                print("→ No es necesario intercambiar")

    print("\n==============================")
    print("ORDENAMIENTO FINALIZADO")
    print("==============================")
    print("Lista ordenada:", lista)

    return lista


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("==========================================")
print(" ORDENAMIENTO POR INTERCAMBIO")
print("==========================================")

print("\nEjemplo práctico:")
print("Ordenar precios de productos de una tienda.")

# Solicitar cantidad de productos
cantidad = int(input("\n¿Cuántos precios deseas ingresar?: "))

precios = []

# Captura de datos
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio #{i+1}: "))
    precios.append(precio)

# Mostrar lista ingresada
print("\nPrecios ingresados:")
print(precios)

# Ejecutar ordenamiento
intercambio_paso_a_paso(precios)