import random

# El sistema selecciona un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Mensaje inicial
print("\n¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

# Inicializar variables
intentos = 0
adivinado = False

# Bucle para adivinar
while not adivinado:
    user_guess = int(input("Ingresa un número: "))
    intentos += 1

    if user_guess == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        adivinado = True
    elif user_guess > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print("El número es mayor. Intenta de nuevo.")
