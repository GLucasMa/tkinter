import tkinter as tk

class Calculadora2:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 2")

        self.label_valor1 = tk.Label(root, text="Valor 1:")
        self.label_valor1.place(x=60,y=70)
        self.label_valor2 = tk.Label(root, text="Valor 2:")
        self.label_valor2.place(x=60,y=110)
        self.label_resultado = tk.Label(root, text="Resultado:")
        self.label_resultado.place(x=60,y=150)
        self.label_operaciones = tk.Label(root, text="Operaciones:")
        self.label_operaciones.place(x=350,y=50)

        self.entry_valor1 = tk.Entry(root)
        self.entry_valor1.place(x=140,y=70)
        self.entry_valor2 = tk.Entry(root)
        self.entry_valor2.place(x=140,y=110)
        self.entry_resultado = tk.Entry(root, state="readonly")
        self.entry_resultado.place(x=140,y=150)

        self.operacion = tk.StringVar()
        self.radio_sumar = tk.Radiobutton(root, text="Sumar", variable=self.operacion, value="suma")
        self.radio_sumar.place(x=350,y=80)
        self.radio_restar = tk.Radiobutton(root, text="Restar", variable=self.operacion, value="resta")
        self.radio_restar.place(x=350,y=110)
        self.radio_multiplicar = tk.Radiobutton(root, text="Multiplicar", variable=self.operacion, value="multiplicacion")
        self.radio_multiplicar.place(x=350,y=140)
        self.radio_dividir = tk.Radiobutton(root, text="Dividir", variable=self.operacion, value="division")
        self.radio_dividir.place(x=350,y=170)

        self.btn_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=200,y=200)

    def calcular(self):
        valor1 = float(self.entry_valor1.get())
        valor2 = float(self.entry_valor2.get())
        operacion = self.operacion.get()

        if operacion == "suma":
            resultado = valor1 + valor2
        elif operacion == "resta":
            resultado = valor1 - valor2
        elif operacion == "multiplicacion":
            resultado = valor1 * valor2
        elif operacion == "division":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                resultado = "Error: División por cero"
        else:
            resultado = "Operación no válida"

        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, str(resultado))
        self.entry_resultado.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    app = Calculadora2(root)
    root.mainloop()
