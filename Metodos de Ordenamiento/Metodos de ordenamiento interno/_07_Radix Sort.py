# ============================================================
# ALGORITMO RADIX SORT
# Ejemplo práctico:
# Ordenar números de guía de una empresa de paquetería
#
# El programa:
# 2. Muestra cada paso del algoritmo.
# 3. Enseña cómo se distribuyen los números en cubetas.
# 4. Muestra el resultado después de cada dígito.
# ============================================================


def radix_sort_paso_a_paso(lista):

    print("\n================================")
    print("INICIANDO RADIX SORT")
    print("================================")

    # Encontrar el número más grande
    maximo = max(lista)

    print(f"\nNúmero más grande encontrado: {maximo}")

    # Comenzamos con las unidades
    posicion = 1

    paso = 1

    while maximo // posicion > 0:

        print("\n" + "=" * 50)
        print(f"PASO {paso}")
        print("=" * 50)

        if posicion == 1:
            print("Ordenando por UNIDADES")

        elif posicion == 10:
            print("Ordenando por DECENAS")

        elif posicion == 100:
            print("Ordenando por CENTENAS")

        elif posicion == 1000:
            print("Ordenando por MILLARES")

        else:
            print(f"Ordenando por posición {posicion}")

        # Crear 10 cubetas (0-9)
        cubetas = [[] for _ in range(10)]

        print("\nDistribuyendo elementos:")

        # Distribuir los números
        for numero in lista:

            digito = (numero // posicion) % 10

            cubetas[digito].append(numero)

            print(
                f"Número {numero} -> "
                f"Cubeta {digito}"
            )

        # Mostrar cubetas
        print("\nContenido de las cubetas:")

        for i in range(10):
            print(f"Cubeta {i}: {cubetas[i]}")

        # Reconstruir la lista
        lista = []

        print("\nReconstruyendo la lista:")

        for i in range(10):

            for numero in cubetas[i]:

                lista.append(numero)

        print(lista)

        posicion *= 10
        paso += 1

    return lista


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 60)
print("            ORDENAMIENTO RADIX SORT")
print("=" * 60)

print("\nEjemplo práctico:")
print("Ordenar números de guía de paquetería.")

cantidad = int(
    input("\n¿Cuántos números desea ingresar?: ")
)

numeros = []

for i in range(cantidad):

    numero = int(
        input(f"Ingrese el número #{i+1}: ")
    )

    while numero < 0:
        print("Radix Sort tradicional trabaja con enteros positivos.")
        numero = int(input("Ingrese nuevamente: "))

    numeros.append(numero)

print("\nLista original:")
print(numeros)

resultado = radix_sort_paso_a_paso(numeros)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Lista ordenada:")
print(resultado)