calificacion = 10

#podemos usar ternarios para abreviar esto:

# color = None
# if calificacion >= 7:
#     color = 'verde'
# else:
#     color = 'rojo'

#Al utilizar el ternario el else es obligatorio
color = 'Verde' if calificacion >= 7 else 'Rojo'


print(calificacion, color)