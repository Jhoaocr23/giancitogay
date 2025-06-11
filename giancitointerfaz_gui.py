import tkinter as tk
from tkinter import messagebox

# Funciones matemáticas
def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función para calcular
def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operacion = operacion_var.get()

        if operacion == "Suma":
            resultado = suma(a, b)
        elif operacion == "Resta":
            resultado = resta(a, b)
        elif operacion == "Multiplicación":
            resultado = multiplicacion(a, b)
        elif operacion == "División":
            resultado = division(a, b)
        else:
            resultado = "Operación no válida"

        resultado_var.set(f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Simple")
root.geometry("300x300")
root.configure(bg="white")

# Entradas
tk.Label(root, text="Primer número:", bg="white").pack(pady=(10, 0))
entry_a = tk.Entry(root, bg="white", fg="black", insertbackground="black")
entry_a.pack(pady=5)

tk.Label(root, text="Segundo número:", bg="white").pack()
entry_b = tk.Entry(root, bg="white", fg="black", insertbackground="black")
entry_b.pack(pady=5)

# Menú de operaciones
tk.Label(root, text="Operación:", bg="white").pack()
operacion_var = tk.StringVar(value="Suma")
menu = tk.OptionMenu(root, operacion_var, "Suma", "Resta", "Multiplicación", "División")
menu.configure(bg="lightgray", fg="black")
menu.pack(pady=5)

# Botón calcular
tk.Button(root, text="Calcular", bg="gray", fg="white", command=calcular).pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
tk.Label(root, textvariable=resultado_var, bg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
