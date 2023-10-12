#lista = list()
#indices    0       1   2      3
lista = ['String', 10, 77.2, True]
#Crear listas que sólo almacenen un tipo de valor

lista_cursos = ['Python', 'Django',  'Flask', 'Java']
lista_cursos[1] = 'Rust'

primer_curso = lista_cursos[0]
ultimo_curso = lista_cursos[-1]

print(lista_cursos)
print("Primer curso: " + primer_curso)
print("Último curso: " + ultimo_curso)