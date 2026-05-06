# ==========================================
# FILTRADO, PREDICCIÓN Y SUAVIZADO (HMM)
# EJEMPLO: ROBOT ASPIRADORA
# ==========================================

# Estados ocultos
states = ["L", "C"]  # Sala, Cocina

# ==========================================
# PASO 1: MODELO
# ==========================================

# Probabilidad inicial
prior = {"L": 0.6, "C": 0.4}

# Transición P(Xt | Xt-1)
transition = {
    "L": {"L": 0.7, "C": 0.3},
    "C": {"L": 0.4, "C": 0.6}
}

# Sensor P(E | X)
sensor = {
    "L": {"D": 0.2, "L": 0.8},  # Sala casi limpia
    "C": {"D": 0.7, "L": 0.3}   # Cocina más sucia
}


# ==========================================
# PASO 2: NORMALIZAR
# ==========================================
def normalize(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}


# ==========================================
# PASO 3: FILTRADO (FORWARD)
# ==========================================
def filtering(observations):
    print("\n=== FILTRADO ===")

    belief = prior.copy()
    history = []

    for t, obs in enumerate(observations):
        print(f"\nTiempo {t+1}, Observación: {obs}")

        # Predicción
        pred = {}
        for s in states:
            pred[s] = sum(transition[prev][s] * belief[prev] for prev in states)

        print("Predicción:", pred)

        # Corrección con evidencia
        for s in states:
            pred[s] *= sensor[s][obs]

        belief = normalize(pred)

        print("Belief actualizado:", belief)

        history.append(belief.copy())

    return history


# ==========================================
# PASO 4: PREDICCIÓN FUTURA
# ==========================================
def prediction(belief, steps):
    print("\n=== PREDICCIÓN ===")

    current = belief.copy()

    for i in range(steps):
        next_belief = {}
        for s in states:
            next_belief[s] = sum(transition[prev][s] * current[prev] for prev in states)

        current = normalize(next_belief)

        print(f"Paso futuro {i+1}: {current}")

    return current


# ==========================================
# PASO 5: SUAVIZADO (BACKWARD SIMPLE)
# ==========================================
def smoothing(observations):
    print("\n=== SUAVIZADO ===")

    forward = filtering(observations)

    backward = {"L": 1.0, "C": 1.0}
    smoothed = []

    for t in reversed(range(len(observations))):
        f = forward[t]

        sm = {}
        for s in states:
            sm[s] = f[s] * backward[s]

        sm = normalize(sm)
        smoothed.insert(0, sm)

        print(f"Tiempo {t+1}: {sm}")

        # actualizar backward
        new_backward = {}
        for s in states:
            new_backward[s] = sum(
                transition[s][s2] * sensor[s2][observations[t]] * backward[s2]
                for s2 in states
            )
        backward = new_backward

    return smoothed


# ==========================================
# PASO 6: ENTRADA INTERACTIVA
# ==========================================
print("Observaciones posibles: D (Sucio), L (Limpio)")

n = int(input("¿Cuántas observaciones?: "))

observations = []
for i in range(n):
    obs = input(f"Observación {i+1}: ")
    observations.append(obs)


# ==========================================
# PASO 7: EJECUCIÓN
# ==========================================
history = filtering(observations)

# última creencia
last_belief = history[-1]

# predicción
future_steps = int(input("\n¿Cuántos pasos futuros predecir?: "))
prediction(last_belief, future_steps)

# suavizado
smoothing(observations)