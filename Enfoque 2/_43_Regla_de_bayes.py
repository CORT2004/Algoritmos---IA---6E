# ==========================================
# REGLA DE BAYES - DETECCIÓN DE FRAUDE
# ==========================================

# ==========================================
# PASO 1: FUNCIÓN DE BAYES CON TRAZADO

def bayes(P_F, P_A_given_F, P_A_given_not_F, trace=True):
    """
    Calcula P(F | A) usando Regla de Bayes
    """

    print("\n=== REGLA DE BAYES ===")

    # Paso 1: Probabilidad complementaria
    P_not_F = 1 - P_F
    if trace:
        print(f"Paso 1: P(no F) = 1 - P(F) = {P_not_F}")

    # Paso 2: Probabilidad total de A
    P_A = (P_A_given_F * P_F) + (P_A_given_not_F * P_not_F)
    if trace:
        print("\nPaso 2: P(A) = P(A|F)*P(F) + P(A|¬F)*P(¬F)")
        print(f"P(A) = ({P_A_given_F} * {P_F}) + ({P_A_given_not_F} * {P_not_F}) = {P_A}")

    # Paso 3: Aplicar Bayes
    P_F_given_A = (P_A_given_F * P_F) / P_A
    if trace:
        print("\nPaso 3: Aplicar Bayes")
        print("P(F|A) = [P(A|F)*P(F)] / P(A)")
        print(f"P(F|A) = ({P_A_given_F} * {P_F}) / {P_A} = {P_F_given_A}")

    return P_F_given_A


# ==========================================
# PASO 2: ENTRADA INTERACTIVA

print("=== DETECCIÓN DE FRAUDE ===")

P_F = float(input("P(F) (probabilidad de fraude): "))
P_A_given_F = float(input("P(A|F) (detección si es fraude): "))
P_A_given_not_F = float(input("P(A|¬F) (falso positivo): "))


# ==========================================
# PASO 3: EJECUCIÓN

resultado = bayes(P_F, P_A_given_F, P_A_given_not_F)

print("\n=== RESULTADO FINAL ===")
print(f"P(F|A) = {resultado}")