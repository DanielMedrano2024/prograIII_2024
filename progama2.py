class Articulo:
    def __init__(self, tipo, especificacion, precio_compra):
        self.tipo = tipo  
        self.especificacion = especificacion  
        self.precio_compra = precio_compra  
        self.precio_venta = round(precio_compra * 1.30, 2)  
        
        
        if tipo == "cuaderno":
            self.marca = "HOJITAS"
        elif tipo == "lapiz":
            self.marca = "RAYAS"

    def __str__(self):
      
        return (f"Tipo: {self.tipo.capitalize()}\nEspecificación: {self.especificacion}\nMarca: {self.marca}\n"
                f"Precio de Compra: ${self.precio_compra}\nPrecio de Venta: ${self.precio_venta}")


print("Registro de Cuadernos:")
tipo = "cuaderno"
especificacion = input("Ingrese la especificación del cuaderno (50 hojas o 100 hojas): ")
precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))


cuaderno = Articulo(tipo, especificacion, precio_compra)


print("\nRegistro de Lápices:")
tipo = "lapiz"
especificacion = input("Ingrese la especificación del lápiz (grafito o colores): ")
precio_compra = float(input("Ingrese el precio de compra del lápiz: "))


lapiz = Articulo(tipo, especificacion, precio_compra)


print("\nInformación del cuaderno registrado:")
print(cuaderno)

print("\nInformación del lápiz registrado:")
print(lapiz)
