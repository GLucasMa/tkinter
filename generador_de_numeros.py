import tkinter as tk
import random

class GeneradorNumeros:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Números")

        self.label_numero1 = tk.Label(root, text="Número 1:")
        self.label_numero1.place(x=30, y=30)
        self.label_numero2 = tk.Label(root, text="Número 2:")
        self.label_numero2.place(x=30, y=60)
        self.label_numero_generado = tk.Label(root, text="Número Generado:")
        self.label_numero_generado.place(x=30, y=90)

        self.spinbox_numero1 = tk.Spinbox(root, from_=1, to=100)
        self.spinbox_numero1.place(x=150, y=30)

        self.spinbox_numero2 = tk.Spinbox(root, from_=1, to=100)
        self.spinbox_numero2.place(x=150, y=60)
        
        self.lineEdit_numero_generado = tk.Entry(root, state="readonly")
        self.lineEdit_numero_generado.place(x=150, y=90)

        self.btn_generar = tk.Button(root, text="Generar", command=self.generar_numero)
        self.btn_generar.place(x=130, y=130)

    def generar_numero(self):
        numero1 = int(self.spinbox_numero1.get())
        numero2 = int(self.spinbox_numero2.get())

        if numero1 <= numero2:
            numero_generado = random.randint(numero1, numero2)
            self.lineEdit_numero_generado.config(state="normal")
            self.lineEdit_numero_generado.delete(0, tk.END)
            self.lineEdit_numero_generado.insert(0, str(numero_generado))
            self.lineEdit_numero_generado.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x300')
    app = GeneradorNumeros(root)
    root.mainloop()
