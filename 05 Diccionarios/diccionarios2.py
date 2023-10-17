elementos = {}

elementos['nombre'] = 'Cody'
elementos[(1,2)] = 'La llave es una tupla'

elementos['nombre'] = 'Fulanito'

#podemos conocer la longitud del diccionario
print(elementos['nombre'])
print(len(elementos))

#si al definir un diccionario duplicamos una llave, dicha llave obtendrá el valor de la última vez invocada
diccionario = {'a':1, 'b':2, 'a':4}
print(diccionario)

#a partir de python 3.7 los diccionarios conservan el orden con respecto a las llaves en el cual fueron definidas
valor = diccionario['b']
print(valor)
#podemos saber si una llave existe en el diccionario con la palabra reservada in
print('z' in diccionario)

#podemos usar get para obtener un valor de forma segura
valorget = diccionario.get('b')

#si la llave no existe retorna none en vez de un error
valorget = diccionario.get('z')

#podemos darle un valor default en caso de que no exista la llave, el valor default puede ser de cualquier tipo: string, int, float, tupla, etc
valorget = diccionario.get('x', 'la llave no existe en el diccionario')

#podemos usar setdefault para agregar un valor en caso de que la llave no exista
valorget = diccionario.setdefault('e', 5)

print(valorget)
print(diccionario)