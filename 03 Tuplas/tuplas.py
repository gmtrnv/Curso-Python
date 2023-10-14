#Las listas se pueden modificar en tiempo de ejecución
#Las tuplas son inmutables, pero pueden almacenar cualquier tipo de datos, string, int, float, listas y tuplas
tupla = ('String', 10, 16.22, True, [11, 22], ('a', 22))
print(tupla)

#aunque son inmutables, podemos agregarle más datos, pero no modificar dichos datos
nueva_tupla = ('algo mas', 88)
tupla += nueva_tupla
print(tupla)