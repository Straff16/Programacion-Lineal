import pulp

"""
Integrantes: 
Paez, Eduardo 30.334.360
Madriz, Francisco 28.480.459
"""

def metodo_esquina_noroeste(rendimiento, tareas, trabajadores):
    
    # Creamos el programación lineal
    problema = pulp.LpProblem("Problema de Transporte", pulp.LpMinimize)
    
    # Creamos una variable de desición
    variables = []
    for i in range(len(rendimiento)):
        fila = []
        for j in range(len(tareas)):
            variable = pulp.LpVariable(f"X_{i}_{j}", lowBound=0, cat='Integer')
            fila.append(variable)
        variables.append(fila)
    
    # Definimos la función objetivo
    objetivo = pulp.lpSum([trabajadores[i][j] * variables[i][j] for i in range(len(rendimiento)) for j in range(len(tareas))])
    problema += objetivo
    
    # Definimos las restricciones de rendimiento
    for i in range(len(rendimiento)):
        restriccion_oferta = pulp.lpSum([variables[i][j] for j in range(len(tareas))])
        problema += restriccion_oferta == rendimiento[i]
    
    # Definimos las restricciones de tareas
    for j in range(len(tareas)):
        restriccion_demanda = pulp.lpSum([variables[i][j] for i in range(len(rendimiento))])
        problema += restriccion_demanda == tareas[j]
    
    problema.solve()
    
    print("Status:", pulp.LpStatus[problema.status])
            
    for i in range(len(rendimiento)):
        for j in range(len(tareas)):
            print(f"{variables[i][j].varValue}\t", end="")
        print()
            
    print("Costo optimizado =", pulp.value(problema.objective))


CapacTrab = [20, 30, 10]
tareas = [15, 25, 20, 10]
trabajadores = [
    [10, 7, 5, 12],
    [6, 2, 9, 11],
    [8, 6, 4, 14]
]

metodo_esquina_noroeste(CapacTrab, tareas, trabajadores)
