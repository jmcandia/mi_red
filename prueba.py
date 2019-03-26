import math
def promedio_std(lista):
    suma = 0
    for el in lista:
        suma += el
    promedio = suma / len(lista)
    suma = 0
    for el in lista:
        suma += (el - promedio) ** 2
    std = math.sqrt(suma / len(lista))
    return (promedio, std)

def color_frecuente(lista):
    sort_order = {'azul':0,'rojo':1,'verde':2,'amarillo':4}
    colores = []
    frecuente = []
    for el in lista:
        if el not in colores:
            colores.append(el)
    for color in colores:
        frecuente.append([color, lista.count(color)])
    frecuente.sort(key=lambda frecuente:sort_order[frecuente[0]])
    mayor = frecuente[0]
    for el in frecuente:
        if el[1] > mayor[1]:
            mayor = el
    return mayor

def busca_minas(tablero, i, j):
	if 0 <= i and i < len(tablero) and 0 <= j and j < len(tablero[0]):
		print(tablero)


tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]


print(promedio_std( [61, 38, 32, 48, 85, 57, 18, 5, 95, 12]))