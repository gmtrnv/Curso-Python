#los diccionarios son mutables
#no corresponden a un índice, sino a una llave
#una llave  puede ser cualquier tipo inmutable, string, tupla
#toda llave debe tener un valor y todo valor debe tener una llave
#se puede declarar con {}
diccionario = {}
#o con el método dict()
diccionario = dict()
#{llave:valor, llave:valor}
diccionario = {"total":55, "descuento":True, "subtotal":15}

#podemos usar como llave cualquier estructura inmutable
diccionario = {"total":55, 10:"Curso de Python", (1,2,3):True}

#para recuperar el valor devemos invocar su llave
print(diccionario[(1,2,3)])

print('------------')
#podemos utilizar clases como llaves
usuario = {
    'nombre': 'Fulanito Detal',
    'edad': 24,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': False
    },
    'medallas': ['básico', 'intermedio']
}

#podemos llamar a los valores usando sus llaves
print(usuario['skills']['programacion'])

#podemos agregar valores utilizando una nueva llave
usuario['apellido'] = 'Perez'

#podemos actualizar valores usando una llave existente
usuario['nombre'] = 'Pedro'
print(f'Hola {usuario["nombre"]} {usuario["apellido"]}. Bienvenido, veo que tienes {usuario["edad"]} años.')
print('................')

#podemos obtener todas las llaves de un diccionario usando el método keys()
print(usuario.keys())

#podemos obtener todos los valores de un diccionario usando el método values()
print(usuario.values())

#podemos usar el método items() para recorrer los valores
print(usuario.items())
#esto devuelve un dict_items de tuplas emparejadas
#[(llave1, valor1), (llave2, valor2)]

#podemos transformar ese dict item en lista
valor = list(usuario.items())

#o en tupla
valor = tuple(usuario.items())

#y acceder al primer par de valores
print(valor[0])

#o a los valores como si fueran una matriz
print(valor[1][0])

print('////////////')
#también podemos usar for para recorrer el diccionario e imprimir los pares
for llave, valor in usuario.items():
    print(f'{llave}: {valor}')

print('*************')
#podemos usar el método get para acceder a un valor sin preocuparnos por el error en caso de que no exista la llave
#get(llave,default)
usuario['calificaciones'] = {'matematicas':10, 'literatura':9.8}
favorito = usuario.get('favorito', 'el usuario no ha definido favorito')
calificaciones = usuario.get('calificaciones', {})
if calificaciones:
    for materia, calificacion in calificaciones.items():
        print(f'{materia}: {calificacion} de 10')

print(usuario)
print(favorito)
print(calificaciones)

print('-*-*-*-*-*-*-*-*')

#podemos usar comprhension para crear diccionarios
#lista_variable = [x for x in iterable]
usuarios = ['Eduardo', 'Fernando', 'Fulanito', 'Algunuel']
diccionario = {posicio + 1:nombre
               for posicio, nombre in enumerate(usuarios)}

print(diccionario)