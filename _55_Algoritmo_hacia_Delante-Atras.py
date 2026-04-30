# ==========================================
# ALGORITMO HACIA DELANTE-ATRÁS (HMM)
# EJEMPLO: ACTIVIDAD FÍSICA
# ==========================================

states = ["E", "R"]  # Ejercicio, Reposo


# ==========================================
# PASO 1: MODELO
# ==========================================

# Probabilidad inicial
prior = {"E": 0.5, "R": 0.5}

# Transición
transition = {
    "E": {"E": 0.7, "R": 0.3},
    "R": {"E": 0.4, "R": 0.6}
}

# Sensor
sensor = {
    "E": {"H": 0.8, "N": 0.2},
    "R": {"H": 0.3, "N": 0.7}
}


# ==========================================
# PASO 2: NORMALIZAR
# ==========================================
def normalize(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}


# ==========================================
# PASO 3: FORWARD (α)
# ==========================================
def forward(observations):
    print("\n=== FORWARD ===")

    alpha = []
    belief = prior.copy()

    for t, obs in enumerate(observations):
        print(f"\nTiempo {t+1}, Obs: {obs}")

        new_belief = {}
        for s in states:
            new_belief[s] = sum(
                transition[prev][s] * belief[prev]
                for prev in states
            )
            new_belief[s] *= sensor[s][obs]

        belief = normalize(new_belief)

        print("Alpha:", belief)
        alpha.append(belief.copy())

    return alpha


# ==========================================
# PASO 4: BACKWARD (β)
# ==========================================
def backward(observations):
    print("\n=== BACKWARD ===")

    beta = [{"E": 1.0, "R": 1.0} for _ in observations]

    for t in reversed(range(len(observations) - 1)):
        print(f"\nTiempo {t+1}")

        for s in states:
            beta[t][s] = sum(
                transition[s][s2] *
                sensor[s2][observations[t+1]] *
                beta[t+1][s2]
                for s2 in states
            )

        print("Beta:", beta[t])

    return beta


# ==========================================
# PASO 5: COMBINAR (SUAVIZADO)
# ==========================================
def forward_backward(observations):
    print("\n=== FORWARD-BACKWARD ===")

    alpha = forward(observations)
    beta = backward(observations)

    smoothed = []

    for t in range(len(observations)):
        sm = {}
        for s in states:
            sm[s] = alpha[t][s] * beta[t][s]

        sm = normalize(sm)
        smoothed.append(sm)

        print(f"\nTiempo {t+1} suavizado:", sm)

    return smoothed


# ==========================================
# PASO 6: ENTRADA INTERACTIVA
# ==========================================
print("Observaciones: H (Alto), N (Normal)")

n = int(input("¿Cuántas observaciones?: "))

observations = []
for i in range(n):
    obs = input(f"Observación {i+1}: ")
    observations.append(obs)


# ==========================================
# PASO 7: EJECUCIÓN
# ==========================================
forward_backward(observations)