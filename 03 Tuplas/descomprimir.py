#se pueden "desempaquetar" los valores de una tupla
numeros = (1,2,3,4,5,6,7,8,9,'azul')
#utilizamos * para indicar una lista con el resto de los valores de la tupla
#El * indica una lista para la variable
#uno, dos, tres, cuatro, *resto_valores = numeros

#podemos usar *_ para descartar el resto de valores
#uno, dos, tres, cuatro, *_, penultimo, ultimo = numeros

#podemos usar _ para omitir valores dentro de la lista
uno, _, tres, _, *_, penultimo, ultimo = numeros

print(uno)
#print(dos)
print(tres)
#print(cuatro)
print(penultimo)
print(ultimo)
#aunque _ si es una variable, se usa para "decartar datos", y podemos imprimirla como una variable normal
print(_)