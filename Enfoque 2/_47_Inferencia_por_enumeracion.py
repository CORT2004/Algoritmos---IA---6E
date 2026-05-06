# ==========================================
# INFERENCIA POR ENUMERACIÓN
# ==========================================

from itertools import product

# ==========================================
# PASO 1: DEFINIR LA RED BAYESIANA
# ==========================================
# A = Enfermedad
# B = Fiebre (depende de A)
# C = Dolor de cabeza (depende de A)

parents = {
    "A": [],
    "B": ["A"],
    "C": ["A"]
}


# ==========================================
# PASO 2: TABLAS DE PROBABILIDAD (CPT)
# ==========================================
CPT = {
    # P(A)
    ("A", True): 0.01,
    ("A", False): 0.99,

    # P(B | A)
    ("B", True, True): 0.8,
    ("B", True, False): 0.1,
    ("B", False, True): 0.2,
    ("B", False, False): 0.9,

    # P(C | A)
    ("C", True, True): 0.7,
    ("C", True, False): 0.2,
    ("C", False, True): 0.3,
    ("C", False, False): 0.8
}


# ==========================================
# PASO 3: FUNCIÓN PARA OBTENER PROBABILIDADES
# ==========================================
def get_prob(var, value, assignment):
    """
    Devuelve P(var = value | padres)
    """
    if not parents[var]:  # variable sin padres
        return CPT[(var, value)]

    parent_values = tuple(assignment[p] for p in parents[var])
    return CPT[(var, value, *parent_values)]


# ==========================================
# PASO 4: ENUMERACIÓN (CON TRAZADO)
# ==========================================
def enumerate_all(vars_list, evidence, depth=0):
    """
    Suma sobre variables ocultas mostrando el proceso
    """
    if not vars_list:
        return 1.0

    Y = vars_list[0]
    rest = vars_list[1:]

    indent = "  " * depth

    # Caso 1: variable conocida
    if Y in evidence:
        prob = get_prob(Y, evidence[Y], evidence)
        print(f"{indent}Usando {Y}={evidence[Y]} → {prob}")
        return prob * enumerate_all(rest, evidence, depth+1)

    # Caso 2: variable oculta (enumeración)
    else:
        total = 0
        for y_val in [True, False]:
            print(f"{indent}Probando {Y}={y_val}")
            
            evidence_copy = evidence.copy()
            evidence_copy[Y] = y_val

            prob = get_prob(Y, y_val, evidence_copy)
            subtotal = prob * enumerate_all(rest, evidence_copy, depth+1)

            print(f"{indent}Subtotal con {Y}={y_val} → {subtotal}")
            total += subtotal

        print(f"{indent}Suma total para {Y} → {total}")
        return total


# ==========================================
# PASO 5: FUNCIÓN PRINCIPAL
# ==========================================
def inference_by_enumeration(query, evidence):
    """
    Calcula P(query | evidence)
    """
    vars_list = list(parents.keys())
    Q = {}

    print("\n=== INFERENCIA POR ENUMERACIÓN ===")

    for value in [True, False]:
        print(f"\n--- Evaluando {query} = {value} ---")

        evidence_copy = evidence.copy()
        evidence_copy[query] = value

        Q[value] = enumerate_all(vars_list, evidence_copy)

    # Normalización
    total = Q[True] + Q[False]
    Q[True] /= total
    Q[False] /= total

    print("\n=== RESULTADO FINAL ===")
    print(f"P({query}=True | evidencia) = {Q[True]}")
    print(f"P({query}=False | evidencia) = {Q[False]}")

    return Q


# ==========================================
# PASO 6: ENTRADA INTERACTIVA
# ==========================================
print("Variables disponibles: A (Enfermedad), B (Fiebre), C (Dolor de cabeza)")

query = input("¿Qué variable quieres calcular?: ")

evidence = {}
n = int(input("¿Cuántas evidencias quieres ingresar?: "))

for i in range(n):
    var = input(f"Variable de evidencia {i+1}: ")
    val = input("Valor (True/False): ")
    evidence[var] = True if val == "True" else False


# ==========================================
# PASO 7: EJECUTAR
# ==========================================
inference_by_enumeration(query, evidence)