def crear_matriz(filas, columnas):
    """Crea una matriz bidimensional con valores ingresados por el usuario."""
    matriz = []
    print("Ingresa los valores de la matriz (5x5):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        matriz.append(fila)
    return matriz

def mostrar_sumas(matriz):
    """Calcula y muestra las sumas de las filas y columnas de una matriz."""
    filas = len(matriz)
    columnas = len(matriz[0])

    # Sumar los elementos de cada fila
    print("\nSuma de los elementos de cada fila:")
    for i in range(filas):
        suma_fila = sum(matriz[i])
        print(f"Suma de fila {i+1}: {suma_fila}")

    # Sumar los elementos de cada columna
    print("\nSuma de los elementos de cada columna:")
    for j in range(columnas):
        suma_columna = sum(matriz[i][j] for i in range(filas))
        print(f"Suma de columna {j+1}: {suma_columna}")

# Parámetros
filas = 5
columnas = 5

# Ejecución del programa
matriz = crear_matriz(filas, columnas)
mostrar_sumas(matriz)