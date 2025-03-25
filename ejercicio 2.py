# Inicializar el vector con datos ingresados por el teclado
vector_original = []
print("Ingresa 5 cadenas de caracteres:")
for i in range(5):
    cadena = input(f"Cadena {i + 1}: ")
    vector_original.append(cadena)

# Copiar los elementos del vector en otro vector en orden inverso
vector_inverso = vector_original[::-1]

# Mostrar el vector original y el vector inverso en pantalla
print("\nVector original:", vector_original)
print("Vector inverso:", vector_inverso)
