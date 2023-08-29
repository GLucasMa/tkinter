from itertools import product
import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title("Contador")
root.geometry('700x250')

def sumar():
    numero.set(str(int(numero.get()) + 1))
    return numero

def restar():
    numero.set(str(int(numero.get()) - 1))
    return numero

def reset():
    numero.set(0)
    return numero


label = tk.Label (root, text='Contador')
label.place(x=45, y=100) 

numero = tk.StringVar(root, "0")
num = tk.Entry(root, textvariable= numero)
num.config(state="readonly")
num.place(x=100,y=100)

botonup = ttk.Button(root, text="Count Up", command= sumar)
botonup.place(x=200,y=100)

botondown = ttk.Button(root, text="Count Down", command= restar)
botondown.place(x=300,y=100)

botonres = ttk.Button(root, text="Reset", command= reset)
botonres.place(x=400,y=100)

root.mainloop()