titulo_curso = 'Curso profesional de Python'
#podemos saber la cantidad de veces que existe un string dentro de otro usando el método count
contador = titulo_curso.count('Python')
print(contador)

#también podemos usar la palabra reservada in para retornar un booleano
print('python' in titulo_curso)
#podemos usar los métodos uppper o lower para estándarizar el string
existe = 'python' in titulo_curso.lower()
print(existe)

#también podemos usar not para negar el in
print('CURSO' not in titulo_curso.upper())

#podemos usar el método startswith() para saber si se encuentra el inicio
print(titulo_curso.upper().startswith('CURSO'))

#también podemos usar el método endswith() para saber si finaliza
print(titulo_curso.endswith('Python'))