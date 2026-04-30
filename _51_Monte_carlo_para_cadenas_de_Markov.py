# ==========================================
# MONTE CARLO - CADENA DE MARKOV (CLIMA)
# ==========================================

import random


# ==========================================
# PASO 1: DEFINIR ESTADOS Y TRANSICIONES
# ==========================================

states = ["S", "N", "L"]  # Soleado, Nublado, Lluvioso

# Matriz de transición
transition = {
    "S": {"S": 0.6, "N": 0.3, "L": 0.1},
    "N": {"S": 0.3, "N": 0.4, "L": 0.3},
    "L": {"S": 0.2, "N": 0.3, "L": 0.5}
}


# ==========================================
# PASO 2: FUNCIÓN PARA SIGUIENTE ESTADO
# ==========================================
def next_state(current):
    """
    Selecciona el siguiente estado según probabilidades
    """
    rand = random.random()
    cumulative = 0

    for state, prob in transition[current].items():
        cumulative += prob
        if rand < cumulative:
            return state


# ==========================================
# PASO 3: SIMULACIÓN MONTE CARLO
# ==========================================
def monte_carlo_markov(initial_state, steps, trace=False):
    """
    Simula la cadena de Markov
    """
    current = initial_state
    history = [current]

    print("\n=== SIMULACIÓN MONTE CARLO ===")

    for i in range(steps):
        nxt = next_state(current)

        if trace and i < 10:
            print(f"Día {i+1}: {current} → {nxt}")

        history.append(nxt)
        current = nxt

    return history


# ==========================================
# PASO 4: ESTIMAR PROBABILIDADES
# ==========================================
def estimate_distribution(history):
    """
    Calcula frecuencia de cada estado
    """
    counts = {s: 0 for s in states}

    for h in history:
        counts[h] += 1

    total = len(history)
    probs = {s: counts[s] / total for s in states}

    print("\n=== DISTRIBUCIÓN ESTIMADA ===")
    print(probs)

    return probs


# ==========================================
# PASO 5: ENTRADA INTERACTIVA
# ==========================================
print("Estados disponibles: S (Soleado), N (Nublado), L (Lluvioso)")

initial = input("Estado inicial: ")
steps = int(input("Número de días a simular: "))


# ==========================================
# PASO 6: EJECUCIÓN
# ==========================================
history = monte_carlo_markov(initial, steps, trace=True)
estimate_distribution(history)