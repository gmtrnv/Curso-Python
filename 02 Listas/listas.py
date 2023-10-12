#lista = list()
#indices    0       1   2      3
lista = ['String', 10, 77.2, True]
#Crear listas que sólo almacenen un tipo de valor

lista_cursos = ['Python', 'Django',  'Flask', 'Java', 'Ruby']
#                  0         1          2       3        4
lista_cursos[1] = 'Rust'

#Las sublistas son inclusivas a la izquierda y exclusivas a la derecha
#[start:end]
sub_lista = lista_cursos[0:3]

primer_curso = lista_cursos[0]
ultimo_curso = lista_cursos[-1]

print(sub_lista)
print("Primer curso: " + primer_curso)
print("Último curso: " + ultimo_curso)