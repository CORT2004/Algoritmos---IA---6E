# ==========================================
# REGLA DE LA CADENA - N EVENTOS
# ==========================================
# Este programa permite calcular:
# P(X1, X2, ..., Xn)
# usando la regla de la cadena:
# P(X1) * P(X2|X1) * ... * P(Xn|X1,...,Xn-1)

# ==========================================

# FUNCIÓN PRINCIPAL

# ==========================================
def chain_rule_trace(probabilities, names):
    """
    probabilities: lista de probabilidades
    names: nombres de cada término
    
    Muestra el cálculo paso a paso
    """
    result = 1

    print("\n=== INICIO DEL CÁLCULO ===")

    for i, p in enumerate(probabilities):
        print(f"\nPaso {i+1}:")
        print(f"Se toma {names[i]} = {p}")
        
        result *= p
        
        print(f"Resultado acumulado: {result}")

    print("\n=== RESULTADO FINAL ===")
    print(f"Probabilidad conjunta = {result}")

    return result


# ==========================================
# PASO 1: PEDIR NÚMERO DE EVENTOS
# ==========================================
n = int(input("¿Cuántos eventos quieres calcular?: "))

probabilities = []
names = []


# ==========================================
# PASO 2: INGRESAR PROBABILIDADES
# ==========================================
for i in range(n):
    
    # Primer evento (no es condicional)
    if i == 0:
        name = f"P(X1)"
        p = float(input(f"Ingresa {name}: "))
    
    # Eventos condicionales
    else:
        condicion = ",".join([f"X{j+1}" for j in range(i)])
        name = f"P(X{i+1}|{condicion})"
        p = float(input(f"Ingresa {name}: "))

    probabilities.append(p)
    names.append(name)


# ==========================================
# PASO 3: CALCULAR RESULTADO
# ==========================================
chain_rule_trace(probabilities, names)