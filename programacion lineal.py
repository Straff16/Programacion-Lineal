c = [1, 2, 3] #Funcion objetivo
A = [[1, 1, 1], [2, 3, 1], [3, 2, 1]] #restricciones
b = [6, 15, 12] #limites de las restricciones

# Resolver el problema de programación lineal
x = [0] * len(c) #lista del tamaño de la funcion objetivo
print("\n", x)
for i in range(len(c)):
    for j in range(len(b)):
        x[i] += A[j][i] * b[j] #Guardar en la lista el producto de los coeficientes de las restricciones por los limites de las restricciones
    x[i] /= sum(A[j][i] for j in range(len(A))) #Se divide el producto anterior entre la suma las filas de la matriz A
    print("\n", x)


