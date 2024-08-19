class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo, motor, color, combustible, transmision, precio_compra, origen):
        self.marca = marca 
        self.modelo = modelo  
        self.anio = anio  
        self.tipo = tipo  
        self.motor = motor 
        self.color = color  
        self.combustible = combustible 
        self.transmision = transmision 
        self.origen = origen 
        self.precio_compra = precio_compra  
        self.precio_venta = round(precio_compra * 1.4, 2)  
        
        
        self.ruedas = 4  
        self.capacidad_pasajeros = 5  

    def __str__(self):
     
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\nTipo: {self.tipo}\n"
                f"Motor: {self.motor}\nColor: {self.color}\nCombustible: {self.combustible}\n"
                f"Transmisión: {self.transmision}\nOrigen: {self.origen}\n"
                f"Precio de Compra: ${self.precio_compra}\nPrecio de Venta: ${self.precio_venta}\n"
                f"Ruedas: {self.ruedas}\nCapacidad de Pasajeros: {self.capacidad_pasajeros} personas")


print("Registro de Vehículo:")
marca = input("Ingrese la marca del vehículo: ")
modelo = input("Ingrese el modelo del vehículo: ")
anio = int(input("Ingrese el año del vehículo: "))
tipo = input("Ingrese el tipo de vehículo (sedán, SUV, etc.): ")
motor = input("Ingrese el tipo de motor (eléctrico, gasolina, etc.): ")
color = input("Ingrese el color del vehículo: ")
combustible = input("Ingrese el tipo de combustible (gasolina, diésel, eléctrico): ")
transmision = input("Ingrese el tipo de transmisión (automática, manual): ")
origen = input("Ingrese el origen del vehículo (nacional o importado): ")
precio_compra = float(input("Ingrese el precio de compra del vehículo: "))


vehiculo = Vehiculo(marca, modelo, anio, tipo, motor, color, combustible, transmision, precio_compra, origen)


print("\nInformación del vehículo registrado:")
print(vehiculo)
