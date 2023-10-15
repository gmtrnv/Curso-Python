#los strings en python son inmutables, no se pueden modificar en tiempo de ejecución
#pero podemos concatenarlos a nuevas variables
nombre = 'Fulanito'
apellido = 'Detal'
edad = 82

#podemos concatenar directamente con +
nombre_completo = nombre + ' ' + apellido

#también podemos concatenar con %s
#se crea una plantilla base con %s para strings, luego fuera de la cadena en un paréntesis se agregan las variables
#podemos usar %i para int y %f para floantes
nombre_completo = 'Señor %s %s, que bueno que ya tiene %i de años y mide %f de estatura' %(nombre, apellido, edad, 1.88)

#podemos usar el método format
nombre_completo = 'Su nombre es {} {}. Y tiene {} años'.format(nombre,apellido,edad)

#también podemos nombrar los placeholders
nombre_completo = 'Tiene {años} y se llama {nombre} {primer_apellido}, recuerda {años} años'.format(
    nombre = nombre,
    primer_apellido = apellido,
    años = edad
)

print(nombre_completo)