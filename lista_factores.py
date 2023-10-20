"""
Lista de factores
"""

# Entradas
numero = int(input("¿De qué número desea los factores? "))

# Proceso 
factores = []
for factor in range(1, numero+1):
    if numero % factor == 0:
        factores.append(factor)

# Salidas
print("Los factores de", numero, "son:", factores)
