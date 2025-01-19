# Solicitar el valor de la factura
valor_factura = float(input("Ingrese el valor de la factura: "))

# Pedir el porcentaje de propina
print("¿Qué porcentaje de propina desea dar? Elija entre 15%, 20%, 25%.")
porcentaje = int(input("Ingrese el porcentaje de propina (sin el símbolo %): "))

# Calcular la propina
propina = valor_factura * porcentaje / 100
print(f"El valor de la propina es: {propina:.2f}")

# Preguntar si se desea dividir entre personas
print("Si desea dividir el total entre varias personas, ingrese el número de personas. De lo contrario, ingrese 1.")
numero_personas = int(input("Número de personas: "))

# Calcular el total por persona y el total general
total_general = valor_factura + propina
total_por_persona = total_general / numero_personas

# Mostrar los resultados
print(f"\n--- Resumen ---")
print(f"Valor de la factura: {valor_factura:.2f}")
print(f"Propina total: {propina:.2f}")
print(f"Total a pagar (factura + propina): {total_general:.2f}")
print(f"Total por persona: {total_por_persona:.2f} (dividido entre {numero_personas} personas)")
