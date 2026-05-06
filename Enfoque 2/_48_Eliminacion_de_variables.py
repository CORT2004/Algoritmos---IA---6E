# ==========================================
# ELIMINACIÓN DE VARIABLES
# ==========================================

# Variables:
# R = Lluvia
# S = Sensor
# A = Alarma

# ==========================================
# FACTORES INICIALES
# ==========================================

# P(R)
factor_R = {
    (True,): 0.3,
    (False,): 0.7
}

# P(S | R)
factor_S = {
    (True, True): 0.9,
    (True, False): 0.2,
    (False, True): 0.1,
    (False, False): 0.8
}

# P(A | S)
factor_A = {
    (True, True): 0.8,
    (True, False): 0.1,
    (False, True): 0.2,
    (False, False): 0.9
}


# ==========================================
# MULTIPLICACIÓN DE FACTORES
# ==========================================
def multiply_factors(f1, vars1, f2, vars2):
    new_vars = list(dict.fromkeys(vars1 + vars2))
    result = {}

    for k1, v1 in f1.items():
        for k2, v2 in f2.items():
            assignment = {}

            for i, var in enumerate(vars1):
                assignment[var] = k1[i]

            for i, var in enumerate(vars2):
                assignment[var] = k2[i]

            new_key = tuple(assignment[var] for var in new_vars)
            result[new_key] = v1 * v2

    return result, new_vars


# ==========================================
# ELIMINAR VARIABLE (SUMAR)
# ==========================================
def sum_out(factor, vars_list, var):
    index = vars_list.index(var)
    new_vars = vars_list[:index] + vars_list[index+1:]
    result = {}

    for key, value in factor.items():
        new_key = key[:index] + key[index+1:]
        result[new_key] = result.get(new_key, 0) + value

    return result, new_vars


# ==========================================
# NORMALIZAR
# ==========================================
def normalize(factor):
    total = sum(factor.values())
    return {k: v/total for k, v in factor.items()}


# ==========================================
# FUNCIÓN PRINCIPAL CON TRAZADO
# ==========================================
def variable_elimination(query, evidence):
    print("\n=== ELIMINACIÓN DE VARIABLES (ALARMA) ===")

    factors = [
        (factor_R, ["R"]),
        (factor_S, ["S", "R"]),
        (factor_A, ["A", "S"])
    ]

    # Aplicar evidencia
    print("\nPaso 1: Aplicar evidencia")
    new_factors = []

    for factor, vars_list in factors:
        new_factor = {}
        for key, val in factor.items():
            valid = True
            for i, var in enumerate(vars_list):
                if var in evidence and key[i] != evidence[var]:
                    valid = False
            if valid:
                new_factor[key] = val

        print(f"Factor reducido {vars_list}: {new_factor}")
        new_factors.append((new_factor, vars_list))

    factors = new_factors

    # Variables ocultas
    hidden_vars = ["R", "S", "A"]
    hidden_vars.remove(query)
    for ev in evidence:
        if ev in hidden_vars:
            hidden_vars.remove(ev)

    print("\nPaso 2: Variables a eliminar:", hidden_vars)

    # Eliminación
    for var in hidden_vars:
        print(f"\nEliminando: {var}")

        related = []
        others = []

        for f in factors:
            if var in f[1]:
                related.append(f)
            else:
                others.append(f)

        f_mult, vars_mult = related[0]
        for f2, vars2 in related[1:]:
            f_mult, vars_mult = multiply_factors(f_mult, vars_mult, f2, vars2)

        print("Factor combinado:", f_mult)

        f_sum, vars_sum = sum_out(f_mult, vars_mult, var)

        print("Después de eliminar:", f_sum)

        factors = others + [(f_sum, vars_sum)]

    # Multiplicación final
    print("\nPaso 3: Multiplicación final")

    f_final, vars_final = factors[0]
    for f2, vars2 in factors[1:]:
        f_final, vars_final = multiply_factors(f_final, vars_final, f2, vars2)

    print("Antes de normalizar:", f_final)

    result = normalize(f_final)

    print("\n=== RESULTADO FINAL ===")
    print(result)

    return result


# ==========================================
# ENTRADA INTERACTIVA
# ==========================================
print("Variables: R (Lluvia), S (Sensor), A (Alarma)")

query = input("Variable a consultar: ")

evidence = {}
n = int(input("¿Cuántas evidencias?: "))

for i in range(n):
    var = input(f"Variable {i+1}: ")
    val = input("Valor (True/False): ")
    evidence[var] = True if val == "True" else False


# ==========================================
# EJECUCIÓN
# ==========================================
variable_elimination(query, evidence)