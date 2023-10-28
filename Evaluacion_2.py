import matplotlib.pyplot as plt
import numpy as np
from pulp import LpMaximize, LpProblem, LpStatus, LpVariable

"""
Integrantes: 
Paez, Eduardo 30.334.360
Madriz, Francisco 28.480.459
"""

# Crear el problema
problema = LpProblem("Problema de Programación Lineal", LpMaximize)

# Definir las variables de decisión
X1 = LpVariable("X1", lowBound=0)
X2 = LpVariable("X2", lowBound=0)

# Definir la función objetivo
problema += 40*X1 + 18*X2, "ZMAX"

# Definir las restricciones
problema += 16*X1 + 2*X2 <= 700, "Restricción 1"
problema += 6*X1 + 3*X2 <= 612, "Restricción 2"
problema += X1 <= 80, "Restricción 3"
problema += X2 <= 120, "Restricción 4"

# Resolver el problema
problema.solve()

# Imprimir el estado de la solución
print("Estado: ", LpStatus[problema.status])

# Imprimir los valores de las variables de decisión
for variable in problema.variables():
    print(variable.name, "=", variable.varValue)

# Imprimir el valor de la función objetivo
print("Valor de la función objetivo: ", problema.objective.value())

# Crear la gráfica
x = np.linspace(0, 80, 100)
y = (700 - 16*x) / 2

# Graficar las restricciones
plt.plot(x, y, label='Restricción 1')

x = np.linspace(0, 80, 100)
y = (612 - 6*x) / 3

plt.plot(x, y, label='Restricción 2')

x = np.linspace(0, 80, 100)
y = np.minimum(120, x*0)

plt.plot(x, y, label='Restricción 3')

x = np.linspace(0, 120, 100)
y = np.minimum(80, x*0)

plt.plot(y, x, label='Restricción 4')

# Graficar la región factible
x = np.linspace(0, 80, 100)
y = np.minimum((700 - 16*x) / 2, (612 - 6*x) / 3)

plt.fill_between(x, 0, y, alpha=0.2, label='Región Factible')

# Personalizar la gráfica
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Gráfica de Programación Lineal')
plt.legend()

# Mostrar la gráfica
plt.show()