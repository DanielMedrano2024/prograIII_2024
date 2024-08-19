class Perro:
    def __init__(self, nombre, raza, color, edad, peso):  
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad
        self.peso = peso
        self.estado = "NO ATENDIDO"
        self.tamano = "Perro Grande" if peso > 10 else "Perro Pequeño" 

    def __str__(self):  
        return (f"Nombre: {self.nombre}\nRaza: {self.raza}\nColor: {self.color}\n"
                f"Edad: {self.edad}\nPeso: {self.peso}kg\nEstado: {self.estado}\nTamaño: {self.tamano}")


nombre = input("Ingresa el nombre del perro: ")
raza = input("Ingresa la raza del perro: ")
color = input("Ingresa el color del perro: ")
edad = int(input("Ingresa la edad del perro: "))
peso = int(input("Ingresa el peso del perro en kg: "))


perro = Perro(nombre, raza, color, edad, peso)


perro.estado = "ATENDIDO"


print("\nInformación del perro registrado:")
print(perro)
