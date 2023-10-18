#python asigna el primer valor verdadero que se encuentra
variable = 'Cody' or 'CodigoFacilito'

#un string vacío es un resultado falso, por lo que se almacena el siguiente
variable = '' or 'CodigoFacilito'

print(variable)

print('---------------------------')
listado = []
nombre = 'Cody'

# if listado:
#     variable_dos = listado
# else:
#     variable_dos = nombre

variable_dos = listado or nombre

print(variable_dos)