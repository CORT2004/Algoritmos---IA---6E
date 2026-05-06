# ==========================================
# HIPÓTESIS DE MARKOV - ESTADO DE ÁNIMO
# ==========================================

import random


# ==========================================
# PASO 1: DEFINIR ESTADOS Y TRANSICIONES
# ==========================================

states = ["F", "N", "T"]  # Feliz, Neutral, Triste

transition = {
    "F": {"F": 0.6, "N": 0.3, "T": 0.1},
    "N": {"F": 0.3, "N": 0.4, "T": 0.3},
    "T": {"F": 0.2, "N": 0.3, "T": 0.5}
}


# ==========================================
# PASO 2: FUNCIÓN DE TRANSICIÓN
# ==========================================
def next_state(current):
    """
    Determina el siguiente estado SOLO con base en el actual
    (Hipótesis de Markov)
    """
    r = random.random()
    cumulative = 0

    for s, p in transition[current].items():
        cumulative += p
        if r < cumulative:
            return s


# ==========================================
# PASO 3: SIMULACIÓN CON TRAZADO
# ==========================================
def simulate_markov(initial, steps, trace=True):
    """
    Simula el proceso mostrando paso a paso
    """
    current = initial
    history = [current]

    print("\n=== SIMULACIÓN (HIPÓTESIS DE MARKOV) ===")

    for i in range(steps):
        nxt = next_state(current)

        if trace:
            print(f"Paso {i+1}:")
            print(f"Estado actual: {current}")
            print(f"Se calcula siguiente estado usando SOLO este valor")
            print(f"Resultado: {nxt}\n")

        history.append(nxt)
        current = nxt

    return history


# ==========================================
# PASO 4: COMPARACIÓN (CON PASADO COMPLETO)
# ==========================================
def explain_markov_property(history):
    """
    Explica por qué se cumple la hipótesis de Markov
    """
    print("\n=== EXPLICACIÓN ===")

    if len(history) < 3:
        print("Se necesitan más pasos para analizar.")
        return

    print("Observa que para predecir el estado actual:")
    print("NO usamos toda la secuencia pasada")
    print("SOLO el estado inmediatamente anterior\n")

    for i in range(2, min(len(history), 6)):
        print(f"Ejemplo en paso {i}:")
        print(f"Pasado completo: {history[:i]}")
        print(f"Estado previo: {history[i-1]}")
        print(f"Estado actual: {history[i]}")
        print("→ Solo depende del estado previo\n")


# ==========================================
# PASO 5: ENTRADA INTERACTIVA
# ==========================================
print("Estados: F (Feliz), N (Neutral), T (Triste)")

initial = input("Estado inicial: ")
steps = int(input("Número de pasos: "))


# ==========================================
# PASO 6: EJECUCIÓN
# ==========================================
history = simulate_markov(initial, steps, trace=True)

print("Secuencia generada:", history)

explain_markov_property(history)