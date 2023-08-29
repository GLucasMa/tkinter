import tkinter as tk
from tkinter import ttk

def restar():
    producto.set(str(int(producto.get()) - 1))

root= tk.Tk()
root.title("ContDecreciente")
root.geometry('450x250')

label = tk.Label (root, text='contador')

label.place(x=50, y=100)

producto = tk.StringVar(root, "88")
prod = tk.Entry(root, textvariable= producto)
prod.config(state="disabled")
prod.place(x=120,y=100)

botonmas = ttk.Button(root, text="-", command= restar)
botonmas.place(x=300,y=100)

root.mainloop()