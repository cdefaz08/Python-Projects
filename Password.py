import random
import string

# Función para generar la contraseña
def generar_contraseña(longitud, mayusculas, minusculas, numeros, simbolos):
    # Crear una lista de caracteres posibles
    caracteres_posibles = ""
    
    if mayusculas:
        caracteres_posibles = string.ascii_uppercase + caracteres_posibles
    if minusculas:
        caracteres_posibles = string.ascii_lowercase + caracteres_posibles
    if numeros:
        caracteres_posibles = string.digits + caracteres_posibles
    if simbolos:
        caracteres_posibles = string.punctuation + caracteres_posibles
    
    # Verificar si hay caracteres posibles
    if len(caracteres_posibles) == 0:
        return "No has seleccionado ningún tipo de carácter válido."
    
    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
    return contraseña

# Solicitar preferencias al usuario
longitud = int(input("¿Cuántos caracteres deseas para tu contraseña? "))
mayusculas = input("¿Deseas incluir mayúsculas? (s/n): ").lower() == "s"
minusculas = input("¿Deseas incluir minúsculas? (s/n): ").lower() == "s"
numeros = input("¿Deseas incluir números? (s/n): ").lower() == "s"
simbolos = input("¿Deseas incluir símbolos? (s/n): ").lower() == "s"

# Generar la contraseña
contraseña = generar_contraseña(longitud, mayusculas, minusculas, numeros, simbolos)

# Mostrar la contraseña
print(f"Tu contraseña generada es: {contraseña}")
