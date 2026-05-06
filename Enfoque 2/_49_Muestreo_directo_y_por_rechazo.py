# ==========================================
# MUESTREO - SISTEMA DE RECOMENDACIÓN
# ==========================================

import random

# ==========================================
# PASO 1: DEFINIR PROBABILIDADES

# G = gusta género
def sample_G():
    return random.random() < 0.6

# R = ve película
def sample_R(G):
    if G:
        return random.random() < 0.8
    else:
        return random.random() < 0.3

# L = le gusta película
def sample_L(R):
    if R:
        return random.random() < 0.9
    else:
        return random.random() < 0.2


# ==========================================
# PASO 2: MUESTREO DIRECTO

def forward_sampling(n, trace=False):
    samples = []

    for i in range(n):
        G = sample_G()
        R = sample_R(G)
        L = sample_L(R)

        sample = {"G": G, "R": R, "L": L}
        samples.append(sample)

        if trace and i < 5:
            print(f"Muestra {i+1}: {sample}")

    return samples


# ==========================================
# PASO 3: MUESTREO POR RECHAZO

def rejection_sampling(query, evidence, n):
    print("\n=== MUESTREO POR RECHAZO ===")

    samples = forward_sampling(n, trace=True)

    accepted = []
    rejected = 0

    for s in samples:
        if all(s[var] == val for var, val in evidence.items()):
            accepted.append(s)
        else:
            rejected += 1

    print(f"\nAceptadas: {len(accepted)}")
    print(f"Rechazadas: {rejected}")

    if len(accepted) == 0:
        print("No hay muestras válidas")
        return None

    prob = sum(1 for s in accepted if s[query]) / len(accepted)

    print(f"\nP({query}=True | evidencia) ≈ {prob}")
    return prob


# ==========================================
# PASO 4: MUESTREO DIRECTO

def estimate_forward(query, n):
    print("\n=== MUESTREO DIRECTO ===")

    samples = forward_sampling(n, trace=True)

    prob = sum(1 for s in samples if s[query]) / n

    print(f"\nP({query}=True) ≈ {prob}")
    return prob


# ==========================================
# PASO 5: ENTRADA INTERACTIVA

print("Variables: G (Género), R (Ve película), L (Le gusta)")

method = input("Método (1=Directo, 2=Rechazo): ")
query = input("Variable a consultar: ")
n = int(input("Número de muestras: "))

evidence = {}

if method == "2":
    m = int(input("¿Cuántas evidencias?: "))
    for i in range(m):
        var = input(f"Variable {i+1}: ")
        val = input("Valor (True/False): ")
        evidence[var] = True if val == "True" else False


# ==========================================
# PASO 6: EJECUCIÓN

if method == "1":
    estimate_forward(query, n)

elif method == "2":
    rejection_sampling(query, evidence, n)

else:
    print("Opción no válida")