#Input retorna un str
nombre_usuario = input('Escribe tu nombre completo: ')

edad_usuario =int(input('Ingresa tu edad: '))

altura_usuario = float(input('Ingresa tu altura en metros: '))

#autorizacion = input('¿Autorizas el programa (si/no): ')
autorizacion = input('¿Autorizas el programa? (si/no): ') == 'si'

print('\n')
print(type(nombre_usuario))
print('Hola ' + nombre_usuario)
print(type(edad_usuario))
print('Te faltan ' + (str(100 - edad_usuario)) + " años para tener 100")
print(type(altura_usuario))
print('Y necesitarías ' + (str(10 - altura_usuario)) + "m para medir 10 metros de alto")
print(type(autorizacion))
print(autorizacion)
print('\n')