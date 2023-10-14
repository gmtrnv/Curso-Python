lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

#podemos usar la función sort para ordenar la lista
#lista.sort() #por default se ordena de menor a mayor
#lista.sort(reverse=True) #podemos usar la opción reverse para ordenar de Mayor a menor

#podemos usar el metodo copy para copiar una lista
nueva_lista = lista.copy()
nueva_lista.sort()
numero_menor = nueva_lista[0]
numero_mayor = nueva_lista[-1]

print("El número mayor es: ")
print(numero_mayor)
print("El número menor es: ")
print(numero_menor)

print(lista)
#también podemos usar el metodo min y max
print(str(min(lista)) + " MIN")
print(str(max(lista)) + " MAX")

#podemos buscar elementos dentro de una lista
#Retorna un valor booleano TRUE si existe
print(1 in lista)
#y FALSE si no existe
print(66 in lista)

#podemos invertir los valores agregando "not"
print(1 not in lista)
print(66 not in lista)