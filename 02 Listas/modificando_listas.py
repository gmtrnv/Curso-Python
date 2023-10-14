lista_cursos = ['Python', 'Django',  'Flask', 'Java', 'Ruby']
nuevos_cursos = ['Docker', 'C++', 'Javascript']
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.append('MongoDB')
lista_cursos.append('C#')

#podemos insertar elementos en posiciones específicas
lista_cursos.insert(2,'Pygame')

#poodemos combinar listas
lista_cursos.extend(nuevos_cursos)

#podemos quitar elementos de la lista por su contenido
lista_cursos.remove('Flask')

#o por su índice utilizando la palabra reservada del, 0 el primero, -1 el último
del lista_cursos[0]

#o podemos eliminar todos los elementos
lista_cursos.clear()

print(lista_cursos)
print(len(lista_cursos))
