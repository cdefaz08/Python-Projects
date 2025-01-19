tareas = []

# Función para agregar tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada exitosamente.")

def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"Tarea '{tarea}' eliminada exitosamente.")
    else:
        print(f"La tarea '{tarea}' no existe en la lista de tareas.")

# Mostrar las tareas
def mostrar_tareas():
    if tareas:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

# Probar la función
agregar_tarea("Comprar leche")
agregar_tarea("Estudiar Python")
agregar_tarea("leer un libro")

#eliminar tarea
eliminar_tarea("comprar leche")

mostrar_tareas()