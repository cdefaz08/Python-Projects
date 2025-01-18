try:
    divisor = int(input("Enter a number to divide by: "))
    result = 10 / divisor
    print(result)
except ZeroDivisionError as e :
    print("Error: Division by zero")
    print("Ha ocurrido un error", e)
except ValueError as e:
    print("Error: You must enter a number")
    print("Ha ocurrido un error",e)
