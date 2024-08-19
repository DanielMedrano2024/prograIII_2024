#calculadora python
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: División por cero"
    else:
        return x / y

print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación (1/2/3/4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    print(f"{num1} + {num2} = {suma(num1, num2)}")
elif opcion == '2':
    print(f"{num1} - {num2} = {resta(num1, num2)}")
elif opcion == '3':
    print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
elif opcion == '4':
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print("Opción no válida")