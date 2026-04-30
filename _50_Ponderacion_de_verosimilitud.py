# ==========================================
# PONDERACIÓN DE VEROSIMILITUD
# EJEMPLO: DETECCIÓN DE SPAM
# ==========================================

import random

# ==========================================
# PASO 1: DEFINIR PROBABILIDADES

# P(S)
def sample_S():
    return random.random() < 0.4

# P(K | S)
def prob_K_given_S(K, S):
    if S:
        return 0.9 if K else 0.1
    else:
        return 0.2 if K else 0.8

def sample_K(S):
    return random.random() < (0.9 if S else 0.2)

# P(U | S)
def prob_U_given_S(U, S):
    if S:
        return 0.1 if U else 0.9
    else:
        return 0.7 if U else 0.3

def sample_U(S):
    return random.random() < (0.1 if S else 0.7)


# ==========================================
# PASO 2: MUESTREO CON PESOS

def weighted_sample(evidence, trace=False):
    """
    Genera una muestra ponderada
    """
    weight = 1.0
    sample = {}

    # Nodo S
    if "S" in evidence:
        sample["S"] = evidence["S"]
        # actualizar peso
        weight *= 0.4 if evidence["S"] else 0.6
    else:
        sample["S"] = sample_S()

    # Nodo K
    if "K" in evidence:
        sample["K"] = evidence["K"]
        w = prob_K_given_S(evidence["K"], sample["S"])
        weight *= w
    else:
        sample["K"] = sample_K(sample["S"])

    # Nodo U
    if "U" in evidence:
        sample["U"] = evidence["U"]
        w = prob_U_given_S(evidence["U"], sample["S"])
        weight *= w
    else:
        sample["U"] = sample_U(sample["S"])

    if trace:
        print(f"Muestra: {sample}, Peso: {weight}")

    return sample, weight


# ==========================================
# PASO 3: ALGORITMO PRINCIPAL

def likelihood_weighting(query, evidence, n_samples):
    print("\n=== PONDERACIÓN DE VEROSIMILITUD ===")

    weights = {True: 0.0, False: 0.0}

    for i in range(n_samples):
        sample, w = weighted_sample(evidence, trace=(i < 5))

        weights[sample[query]] += w

    # Normalizar
    total = weights[True] + weights[False]
    prob_true = weights[True] / total

    print("\nPesos acumulados:", weights)
    print(f"\nP({query}=True | evidencia) ≈ {prob_true}")

    return prob_true


# ==========================================
# PASO 4: ENTRADA INTERACTIVA
# ==========================================
print("Variables: S (Spam), K (Palabras clave), U (Importante)")

query = input("Variable a consultar: ")
n = int(input("Número de muestras: "))

evidence = {}
m = int(input("¿Cuántas evidencias?: "))

for i in range(m):
    var = input(f"Variable {i+1}: ")
    val = input("Valor (True/False): ")
    evidence[var] = True if val == "True" else False


# ==========================================
# PASO 5: EJECUCIÓN
# ==========================================
likelihood_weighting(query, evidence, n)