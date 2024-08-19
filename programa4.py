class Dispositivo:
    def __init__(self, tipo, modelo, memoria, procesador, pantalla, almacenamiento, precio_compra):
        self.tipo = tipo  
        self.modelo = modelo  
        self.memoria = memoria  
        self.procesador = procesador
        self.pantalla = pantalla  
        self.almacenamiento = almacenamiento  
        self.precio_compra = precio_compra  
        self.precio_venta = round(precio_compra * 1.7, 2) 

       
        self.marca = "PHR"  
        self.origen = "Importado"  

    def __str__(self):
       
        return (f"Tipo: {self.tipo.capitalize()}\nModelo: {self.modelo}\nMemoria RAM: {self.memoria}\n"
                f"Procesador: {self.procesador}\nPantalla: {self.pantalla} pulgadas\n"
                f"Almacenamiento: {self.almacenamiento} GB\nPrecio de Compra: ${self.precio_compra}\n"
                f"Precio de Venta: ${self.precio_venta}\nMarca: {self.marca}\nOrigen: {self.origen}")


print("Registro de Dispositivo Electrónico:")
tipo = input("Ingrese el tipo de dispositivo (celular, tablet, portátil): ")
modelo = input("Ingrese el modelO del dispositivo: ")
memoria = input("Ingrese la cantidad de memoria RAM (en GB): ")
procesador = input("Ingrese el tipo de procesador: ")
pantalla = float(input("Ingrese el tamaño de la pantalla (en pulgadas): "))
almacenamiento = int(input("Ingrese la capacidad de almacenamiento (en Gb): "))
precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))


dispositivo = Dispositivo(tipo, modelo, memoria, procesador, pantalla, almacenamiento, precio_compra)


print("\nInformación del dispositivo registrado:")
print(dispositivo)
