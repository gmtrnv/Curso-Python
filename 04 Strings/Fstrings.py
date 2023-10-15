nombre = 'Alguienuel'
apellido = "Apellidez"
edad = 98

#podemos usar fstrings para hacer interpolación
#utiliizamos los nombres directamente de las variables, sólo hay que anteponer una "f" antes del string
#también podemos usar operaciones dentro
nombre_completo = f'Mr. {nombre} {apellido}, tiene {edad}, recuerda {edad} años y mide {1.42}m!! aún le quedan {edad * 2} de años'

#print(nombre_completo)
#se puede imprimir directamente
print(f'Mr. {nombre} {apellido}, tiene {edad}, recuerda {edad} años y mide {1.42}m!! aún le quedan {edad * 2} de años')