#lgoritmo Desviación_Estandar
n = int(input("¿Cuántos valores quieres ingresar?: "))

datos = []

for i in range(1, n + 1):
    valor = float(input(f"Ingresa el valor {i}: "))
    datos.append(valor)
    
sumaDatos = 0
for i in range(n):
    sumaDatos += datos[i]

promedio = sumaDatos / n
print("El promedio es", promedio)

sumatoria = 0
for i in range(n):
    sumatoria += (datos[i] - promedio) ** 2

division = sumatoria / n
desvEst = division ** 0.5
print("La desviación estándar es", desvEst)