add = lambda a , b: a+b
print(add(1,2))

multiply = lambda a , b: a*b
print(multiply(2,3))

#Cuadrado de un numero
numbers = range(13)
squared_numbers = list(map(lambda x: x*x, numbers))
print("Cuadrados:", squared_numbers)

#Numeros pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)