lenguajes = 'Python Ruby Java Rust C++ C'
guiones = 'Python-Ruby-Script-CSharp'
#el metodo split nos permite separar un string para almacenarlo como lista
#por default split separa el string por espacios
listado_lenguajes = lenguajes.split()
#podemos pasarle como argumento el string a través del cuál queramos que separe
listado_lenguajes = guiones.split('-')
#podemos pasarle como segundo argumento  para decirle cuantos slices hacer
listado_lenguajes = lenguajes.split(' ',2)

print(listado_lenguajes)
print('------')

lenguajes_nuevos = ['Python', 'Ruby', 'Java', 'Rust']

#con el metodo join podemos unir un listado, empezamos con el caracter que los separará y luego unimos la lista
cadena_unida = ' '.join(lenguajes_nuevos)
print(cadena_unida)