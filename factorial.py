import tkinter as tk
import math

def calcular_factorial():
    try:
        n = int(entry_n.get())
        factorial = math.factorial(n)
        #                      Borrar anterior
        entry_factorial.delete(0, tk.END) 
        entry_factorial.insert(0, str(factorial))
    except ValueError:
        entry_factorial.delete(0, tk.END)
        entry_factorial.insert(0, "Error: Ingresa un número entero válido")


def siguiente():
    n = int(entry_n.get())
    n += 1
    entry_n.delete(0, tk.END)
    entry_n.insert(0, str(n))
    calcular_factorial()


ventana = tk.Tk()
ventana.title("Factorial")

label_n = tk.Label(ventana, text="n:")
label_n.place(x=50, y=100)

entry_n = tk.Entry(ventana)
entry_n.place(x=80, y=100)
entry_n.insert(0, "1")  

label_factorial = tk.Label(ventana, text="Factorial (n):")
label_factorial.place(x=150, y=100)

entry_factorial = tk.Entry(ventana)
entry_factorial.place(x=200, y=100)

boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente)
boton_siguiente.place(x=300, y=100)

boton_calcular = tk.Button(ventana, command=calcular_factorial)


calcular_factorial()
ventana.geometry('450x250')
ventana.mainloop()
