def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora simple")
    print("Opciones: suma, resta, multiplicacion, division")
    operacion = input("Elige una operación: ").strip().lower()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if operacion == "suma":
        print("Resultado:", suma(a, b))
    elif operacion == "resta":
        print("Resultado:", resta(a, b))
    elif operacion == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif operacion == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida")

if __name__ == "__main__":
    calculadora()