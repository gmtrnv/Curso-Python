diccionario = {'a':1,'b':2,'c':3,'d':4}
del diccionario['b']
valor = diccionario.pop('c')
diccionario.clear()
print(diccionario)
print(valor)