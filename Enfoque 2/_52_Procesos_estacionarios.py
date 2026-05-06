# ==========================================
# PROCESOS ESTACIONARIOS - TRÁFICO DE RED
# ==========================================

import random


# ==========================================
# PASO 1: DEFINIR ESTADOS Y TRANSICIONES
# ==========================================

states = ["B", "M", "A"]  # Bajo, Medio, Alto

transition = {
    "B": {"B": 0.7, "M": 0.2, "A": 0.1},
    "M": {"B": 0.3, "M": 0.4, "A": 0.3},
    "A": {"B": 0.2, "M": 0.3, "A": 0.5}
}


# ==========================================
# PASO 2: SIGUIENTE ESTADO
# ==========================================
def next_state(current):
    r = random.random()
    cumulative = 0

    for s, p in transition[current].items():
        cumulative += p
        if r < cumulative:
            return s


# ==========================================
# PASO 3: SIMULACIÓN DEL PROCESO
# ==========================================
def simulate_process(initial, steps, trace=False):
    """
    Simula el proceso en el tiempo
    """
    current = initial
    history = [current]

    print("\n=== SIMULACIÓN DEL PROCESO ===")

    for i in range(steps):
        nxt = next_state(current)

        if trace and i < 10:
            print(f"Paso {i+1}: {current} → {nxt}")

        history.append(nxt)
        current = nxt

    return history


# ==========================================
# PASO 4: CALCULAR DISTRIBUCIÓN
# ==========================================
def compute_distribution(history):
    counts = {s: 0 for s in states}

    for h in history:
        counts[h] += 1

    total = len(history)
    probs = {s: counts[s] / total for s in states}

    return probs


# ==========================================
# PASO 5: MOSTRAR CONVERGENCIA
# ==========================================
def show_convergence(initial, steps, interval):
    """
    Muestra cómo la distribución se estabiliza
    """
    print("\n=== CONVERGENCIA A ESTACIONARIO ===")

    current = initial
    history = []

    for i in range(steps):
        current = next_state(current)
        history.append(current)

        # Cada cierto intervalo mostramos distribución
        if (i + 1) % interval == 0:
            dist = compute_distribution(history)
            print(f"Iteración {i+1}: {dist}")


# ==========================================
# PASO 6: ENTRADA INTERACTIVA
# ==========================================
print("Estados: B (Bajo), M (Medio), A (Alto)")

initial = input("Estado inicial: ")
steps = int(input("Número de pasos: "))
interval = int(input("Cada cuántos pasos mostrar convergencia: "))


# ==========================================
# PASO 7: EJECUCIÓN
# ==========================================
history = simulate_process(initial, steps, trace=True)

final_dist = compute_distribution(history)

print("\n=== DISTRIBUCIÓN FINAL ===")
print(final_dist)

show_convergence(initial, steps, interval)