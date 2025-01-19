class Vehiculos ():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.available = True

class Persona:
    def __init__(self,nombre,id_persona):
        self.nombre = nombre
        self.id = id_persona

class Concesionario:
    def __init__(self):
        self.vehiculos = []
        self.persona = []
    
    def add_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f" Added \n Marca: {vehiculo.marca} Modelo: {vehiculo.modelo}")

    def add_persona(self, persona):
        self.persona.append(persona)
        print(f" Added \n Persona: {persona.nombre} ID: {persona.id}")

    def remove_persona(self, persona):
        self.persona.remove(persona)
        print(f" Removed \n Persona: {persona.nombre} ID: {persona.id}")
    
    def remove_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)
        print(f" Removed \n Marca: {vehiculo.marca} Modelo: {vehiculo.modelo}")

    def buy_vehiculo(self, vehiculo, persona):
        if vehiculo.available:
            vehiculo.available = False
            print(f"Vehiculo {vehiculo.marca} {vehiculo.modelo} has been sold to {persona.nombre}")
        else:
            print(f"Vehiculo {vehiculo.marca} {vehiculo.modelo} is not available")

    def return_vehiculo(self, vehiculo, persona):
        if vehiculo.available:
            print(f"vehiculo {vehiculo.marca} {vehiculo.modelo} is already available")
        else:
            vehiculo.available = True
            print(f"vehiculo {vehiculo.marca} {vehiculo.modelo} has been returned by {persona.nombre}")

    
    def show_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.marca} Modelo: {vehiculo.modelo} Disponible: {vehiculo.available}")



#create instances for vehiculos
vehiculo1 = Vehiculos("Toyota","Corolla")
vehiculo2 = Vehiculos("Nissan","Sentra")

#create instances for Persona
persona = Persona("John",1)
persona2 = Persona("Jane",2)

#Create a consecionario object
consencionario = Concesionario()

#Add vehiculos and personas
consencionario.add_vehiculo(vehiculo1)
consencionario.add_vehiculo(vehiculo2)
consencionario.add_persona(persona)
consencionario.add_persona(persona2)

consencionario.buy_vehiculo(vehiculo1,persona)

consencionario.show_vehiculos()

print("second stage")

consencionario.return_vehiculo(vehiculo1,persona)

#dysplay vehiculos
consencionario.show_vehiculos()