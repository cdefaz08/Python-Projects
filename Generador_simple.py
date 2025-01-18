def numerors_impares(limit):
    a = 1
    while a <= limit:
        yield a
        a +=2

def numeros_pares(limit):
    a = 0
    while a <= limit:
        yield a
        a += 2

print("Numeros impares")
for num in numerors_impares(10):
    print(num)

print("Numeros pares")
for num in numeros_pares(10):
    print(num)