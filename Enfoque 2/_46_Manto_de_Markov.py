# ==========================================
# MANTO DE MARKOV 
# ==========================================
# Este programa permite:
# 1. Definir una red bayesiana simple
# 2. Elegir una variable objetivo
# 3. Calcular su manto de Markov
# 4. Mostrar el proceso paso a paso

# ==========================================

# FUNCIÓN PARA CALCULAR EL MANTO DE MARKOV

# ==========================================
def markov_blanket_trace(node, parents, children):
    """
    node: variable objetivo
    parents: diccionario {nodo: [padres]}
    children: diccionario {nodo: [hijos]}
    
    Devuelve el manto de Markov mostrando el proceso
    """

    print("\n=== CÁLCULO DEL MANTO DE MARKOV ===")

    # ==========================================
    # PASO 1: PADRES DEL NODO
    
    padres = parents.get(node, [])
    print(f"\nPaso 1: Padres de {node} → {padres}")

    # ==========================================
    # PASO 2: HIJOS DEL NODO
    
    hijos = children.get(node, [])
    print(f"Paso 2: Hijos de {node} → {hijos}")

    # ==========================================
    # PASO 3: PADRES DE LOS HIJOS
    
    padres_hijos = []
    for h in hijos:
        for p in parents.get(h, []):
            if p != node:  # evitar incluir el nodo mismo
                padres_hijos.append(p)

    print(f"Paso 3: Padres de los hijos de {node} → {padres_hijos}")

    # ==========================================
    # PASO 4: UNIÓN DE TODOS
    
    blanket = set(padres + hijos + padres_hijos)

    print(f"\nManto de Markov de {node} = {blanket}")

    return blanket


# ==========================================
# PASO 1: CREAR RED BAYESIANA

n = int(input("¿Cuántas variables (nodos) tiene la red?: "))

nodes = []
parents = {}
children = {}

# Inicializar estructuras
for i in range(n):
    node = input(f"Nombre del nodo {i+1}: ")
    nodes.append(node)
    parents[node] = []
    children[node] = []


# ==========================================
# PASO 2: DEFINIR RELACIONES (PADRES)

print("\nDefine los padres de cada nodo:")

for node in nodes:
    entrada = input(f"Padres de {node} (separados por coma): ")
    
    if entrada.strip() != "":
        lista_padres = [p.strip() for p in entrada.split(",")]
        parents[node] = lista_padres

        # Construir hijos automáticamente
        for p in lista_padres:
            children[p].append(node)


# ==========================================
# PASO 3: ELEGIR VARIABLE OBJETIVO

target = input("\n¿De qué nodo quieres el manto de Markov?: ")

# ==========================================
# PASO 4: CALCULAR MANTO DE MARKOV

markov_blanket_trace(target, parents, children)