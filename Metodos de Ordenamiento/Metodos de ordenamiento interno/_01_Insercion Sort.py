# ==========================================
# INSERTION SORT
# EJEMPLO: ORDENAR CALIFICACIONES
# ==========================================

# ==========================================
# PASO 1: FUNCIÓN DE ORDENAMIENTO
# ==========================================
def insertion_sort(lista, mostrar_pasos=True):
    """
    Ordena una lista usando Insertion Sort
    """

    print("\n=== INICIANDO INSERTION SORT ===")

    # Recorre desde el segundo elemento
    for i in range(1, len(lista)):

        # Elemento a insertar
        clave = lista[i]

        # Índice del elemento anterior
        j = i - 1

        if mostrar_pasos:
            print(f"\nPaso {i}")
            print(f"Elemento a insertar: {clave}")

        # ==================================
        # Mover elementos mayores a la derecha
        # ==================================
        while j >= 0 and lista[j] > clave:

            if mostrar_pasos:
                print(
                    f"Comparando {clave} con {lista[j]} "
                    f"→ {lista[j]} es mayor, se mueve"
                )

            lista[j + 1] = lista[j]
            j -= 1

            if mostrar_pasos:
                print("Estado actual:", lista)

        # ==================================
        # Insertar en la posición correcta
        # ==================================
        lista[j + 1] = clave

        if mostrar_pasos:
            print(
                f"Insertando {clave} en posición {j + 1}"
            )
            print("Lista después de insertar:")
            print(lista)

    return lista


# ==========================================
# PASO 2: ENTRADA INTERACTIVA
# ==========================================
print("=== ORDENAMIENTO DE CALIFICACIONES ===")

cantidad = int(
    input("¿Cuántas calificaciones desea ingresar?: ")
)

calificaciones = []

for i in range(cantidad):
    valor = float(
        input(f"Ingrese la calificación #{i+1}: ")
    )

    calificaciones.append(valor)

# ==========================================
# PASO 3: MOSTRAR LISTA ORIGINAL
# ==========================================
print("\nLista original:")
print(calificaciones)

# ==========================================
# PASO 4: EJECUTAR ALGORITMO
# ==========================================
resultado = insertion_sort(
    calificaciones,
    mostrar_pasos=True
)

# ==========================================
# PASO 5: RESULTADO FINAL
# ==========================================
print("\n=== RESULTADO FINAL ===")
print("Lista ordenada:")
print(resultado)
