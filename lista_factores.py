"""
Lista de factores
"""

# Entradas
numero = int(input("¿De qué número desea los factores? "))

# Proceso 
factores = [1]
if numero % 2 == 0:
    factores.append(2)
if numero % 3 == 0:
    factores.append(3)
if numero % 5 == 0:
    factores.append(5)

# Salidas
print("Los factores de", numero, "son:", factores)
