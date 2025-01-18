#crear un iterador para los numeros impares

#limite
limite = 10

#Crear un iterador
odd_iter = iter(range(1,limite+1,2))

#usar el iterador
for num in odd_iter:
    print(num)