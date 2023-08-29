#Porque tengo que importar como tk y no me deja usar el comando Tk. directamente sobre los metodos o atributos?

import tkinter as tk
from tkinter import ttk

def sumar():
    producto.set(str(int(producto.get()) + 1))

root= tk.Tk()
root.title("contador")
root.geometry('450x250')

label = tk.Label (root, text='contador')

label.place(x=50, y=100)

producto = tk.StringVar(root, "0")
prod = tk.Entry(root, textvariable= producto)
prod.config(state="disabled")
prod.place(x=120,y=100)

botonmas = ttk.Button(root, text="+", command= sumar)
botonmas.place(x=300,y=100)

root.mainloop()