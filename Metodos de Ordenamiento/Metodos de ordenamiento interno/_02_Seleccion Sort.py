# ==========================================
# SELECTION SORT
# EJEMPLO: TIEMPOS DE ENTREGA DE PAQUETES
# ==========================================

# ==========================================
# PASO 1: FUNCIÓN DE ORDENAMIENTO
# ==========================================
def selection_sort(lista, mostrar_pasos=True):
    """
    Ordena una lista utilizando Selection Sort
    """

    n = len(lista)

    print("\n=== INICIANDO SELECTION SORT ===")

    # ======================================
    # Recorremos toda la lista
    # ======================================
    for i in range(n):

        # Suponemos que el mínimo está en i
        indice_minimo = i

        if mostrar_pasos:
            print(f"\nPaso {i+1}")
            print(f"Buscando el menor elemento desde la posición {i}")

        # ======================================
        # Buscar el elemento más pequeño
        # ======================================
        for j in range(i + 1, n):

            if mostrar_pasos:
                print(
                    f"Comparando {lista[j]} con "
                    f"{lista[indice_minimo]}"
                )

            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

                if mostrar_pasos:
                    print(
                        f"Nuevo mínimo encontrado: "
                        f"{lista[indice_minimo]}"
                    )

        # ======================================
        # Intercambiar posiciones
        # ======================================
        lista[i], lista[indice_minimo] = (
            lista[indice_minimo],
            lista[i]
        )

        if mostrar_pasos:
            print(
                f"Intercambiando posición {i} "
                f"con posición {indice_minimo}"
            )
            print("Estado actual:")
            print(lista)

    return lista


# ==========================================
# PASO 2: ENTRADA INTERACTIVA
# ==========================================
print("=== ORDENAMIENTO DE TIEMPOS DE ENTREGA ===")

cantidad = int(
    input("¿Cuántos tiempos desea ingresar?: ")
)

tiempos = []

for i in range(cantidad):

    valor = float(
        input(f"Ingrese el tiempo #{i+1}: ")
    )

    tiempos.append(valor)

# ==========================================
# PASO 3: MOSTRAR DATOS ORIGINALES
# ==========================================
print("\nLista original:")
print(tiempos)

# ==========================================
# PASO 4: EJECUTAR ALGORITMO
# ==========================================
resultado = selection_sort(
    tiempos,
    mostrar_pasos=True
)

# ==========================================
# PASO 5: RESULTADO FINAL
# ==========================================
print("\n=== RESULTADO FINAL ===")
print("Lista ordenada:")

print(resultado)