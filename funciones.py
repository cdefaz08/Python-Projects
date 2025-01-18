def add (a , b):
    return a + b


def substract (a , b):
    return a - b

def multiply (a , b):
    return a * b

def divide (a , b):
    return a / b

def calculator():
    while True:
        print("seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        option = (input("ingresa una opcion: 1,2,3,4,5:"))

        if option == "5":
            print("Saliendo de l calculadora")
            break
            
        if option in ["1","2","3","4"]:
            num1 = float(input("ingresa el primer numero"))
            num2 = float1(input("ingresa el segundo numero"))
            if option == "1":
                print("Resultado: ", add(num1,num2))
            elif option == "2":
                print("Resultado: ", substract(num1,num2)) 
            elif option == "3":
                print("Resultado: ", multiply(num1,num2))
            elif option == "4":
                print("Resultado: ", divide(num1,num2))
        else: 
            print("Opcion invalida")


calculator()
            
