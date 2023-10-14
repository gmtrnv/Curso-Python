lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300]

#la función zip comprime elementos dentro de un objeto de tipo zip
resultado = zip(lista, tupla,lista_2)
#comprimir reduce a su minima expresión los elemenots, haciendo pares por índices dentro de tuplas
#podemos convertir el objeto zip en una lista de tuplas
#resultado = list(resultado)
#o a una tupla de tuplas
resultado = tuple(resultado)

print(resultado)
