def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


#print(factorial(3))

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
number = 0
#print(Fibonacci(number))  

def numeros_nat(n):
    if n == 0:
        return 0
    else:
        return n + numeros_nat(n-1)

print(numeros_nat(4))