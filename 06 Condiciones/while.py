contador = 1
while contador <= 10:
    print(contador)
    contador += 1
print('--------------')
numero = 145281
contador_digitos = 0
#Hay que usar while cuando no sepamos el número de iteraciones
while numero >= 1:
    contador_digitos += 1
    numero /= 10
#podemos usar else porque while usa una confición
else:
    print('fin del ciclo while')
print(contador_digitos)
