# Clase base que puede incluir métodos comunes
class Entidad:
    def mostrar_info(self):
        raise NotImplementedError("Debe implementarse en la clase hija")

    def eliminar(self):
        print(f"{self.__class__.__name__} eliminado.")

# Clase hija para Contacto
class Contacto(Entidad):
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

# Clase hija para AdministradorDeContactos
class AdministradorDeContactos(Entidad):
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos[nombre] = nuevo_contacto
        print(f"Contacto de {nombre} agregado exitosamente.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Contacto encontrado: {nombre}")
            self.contactos[nombre].mostrar_info()
        else:
            print(f"El contacto de {nombre} no existe.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            self.contactos[nombre].eliminar()
            del self.contactos[nombre]
        else:
            print(f"El contacto de {nombre} no existe.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos.values():
                contacto.mostrar_info()
                print("---")
        else:
            print("No hay contactos almacenados.")

# Probar el sistema
admin_contactos = AdministradorDeContactos()
admin_contactos.agregar_contacto("Juan Pérez", "123456789", "juan@ejemplo.com")
admin_contactos.agregar_contacto("Ana Gómez", "987654321", "ana@ejemplo.com")
admin_contactos.mostrar_contactos()

admin_contactos.buscar_contacto("Juan Pérez")
admin_contactos.eliminar_contacto("Ana Gómez")
admin_contactos.mostrar_contactos()
