# ==========================================
# APRENDIZAJE POR REFUERZO PASIVO
# EJEMPLO: ESTUDIANTE
# ==========================================

import random


# ==========================================
# PASO 1: DEFINIR ESTADOS Y RECOMPENSAS
# ==========================================

states = ["E", "D", "A", "R"]

# Recompensas
rewards = {
    "E": -1,   # esfuerzo
    "D": -0.5, # descanso (menos costo)
    "A": 10,   # aprobar
    "R": -10   # reprobar
}

# Transiciones (política fija)
transition = {
    "E": ["E", "A"],   # sigue estudiando o aprueba
    "D": ["D", "R"],   # sigue descansando o reprueba
}


# ==========================================
# PASO 2: GENERAR EPISODIO
# ==========================================
def generate_episode(trace=False):
    """
    Genera un episodio completo
    """
    state = random.choice(["E", "D"])
    episode = []

    if trace:
        print("\n=== NUEVO EPISODIO ===")

    while state not in ["A", "R"]:
        next_state = random.choice(transition[state])

        if trace:
            print(f"{state} → {next_state}")

        episode.append((state, rewards[state]))
        state = next_state

    # estado final
    episode.append((state, rewards[state]))

    if trace:
        print(f"Estado final: {state}")

    return episode


# ==========================================
# PASO 3: CALCULAR RETORNO
# ==========================================
def compute_returns(episode):
    """
    Calcula retorno acumulado
    """
    G = 0
    returns = []

    for state, reward in reversed(episode):
        G = reward + G
        returns.insert(0, (state, G))

    return returns


# ==========================================
# PASO 4: APRENDIZAJE
# ==========================================
def passive_learning(episodes, trace=True):
    """
    Aprende utilidad de estados
    """
    values = {s: 0 for s in states}
    counts = {s: 0 for s in states}

    for i in range(episodes):
        episode = generate_episode(trace=(i < 3))

        returns = compute_returns(episode)

        if trace and i < 3:
            print("Retornos:", returns)

        for state, G in returns:
            values[state] += G
            counts[state] += 1

    # Promedio
    for s in states:
        if counts[s] > 0:
            values[s] /= counts[s]

    print("\n=== UTILIDADES APRENDIDAS ===")
    print(values)

    return values


# ==========================================
# PASO 5: ENTRADA INTERACTIVA
# ==========================================
episodes = int(input("Número de episodios: "))


# ==========================================
# PASO 6: EJECUCIÓN
# ==========================================
passive_learning(episodes)