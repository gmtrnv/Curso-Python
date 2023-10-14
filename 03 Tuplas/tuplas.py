#Las listas se pueden modificar en tiempo de ejecución
#Las tuplas son inmutables, pero pueden almacenar cualquier tipo de datos, string, int, float, listas y tuplas
tupla = ('String', 10, 16.22, True, [11, 22], ('a', 22))
print(tupla)

#aunque son inmutables, podemos agregarle más datos, pero no modificar dichos datos
nueva_tupla = ('algo mas', 88)
tupla += nueva_tupla
print(tupla)

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#se pueden usar índices para acceder a los elementos de las tuplas
print(cursos[-1])

#se pueden crear subtuplas con los msmos métodos vistos en las listas
sub_tupla = cursos[:]
print(sub_tupla)