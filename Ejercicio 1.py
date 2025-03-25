import random

# Definir el vector y llenarlo con valores aleatorios entre 1 y 10
vector_numeros = [random.randint(1, 10) for _ in range(10)]

# Mostrar cada elemento del vector junto con su cuadrado y su cubo
print("Número | Cuadrado | Cubo")
for numero in vector_numeros:
    cuadrado = numero ** 2
    cubo = numero ** 3
    print(f"{numero:6} | {cuadrado:8} | {cubo:4}")
