import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.primer_numero = tk.StringVar()
        self.segundo_numero = tk.StringVar()
        self.resultado = tk.StringVar()

        self.label_primer_numero = tk.Label(root, text="Primer número:")
        self.label_primer_numero.pack()
        self.entry_primer_numero = tk.Entry(root, textvariable=self.primer_numero)
        self.entry_primer_numero.pack()

        self.label_segundo_numero = tk.Label(root, text="Segundo número:")
        self.label_segundo_numero.pack()
        self.entry_segundo_numero = tk.Entry(root, textvariable=self.segundo_numero)
        self.entry_segundo_numero.pack()

        self.label_resultado = tk.Label(root, text="Resultado:")
        self.label_resultado.pack()
        self.entry_resultado = tk.Entry(root, textvariable=self.resultado, state="readonly")
        self.entry_resultado.pack()

        self.btn_suma = tk.Button(root, text="+", command=self.sumar)
        self.btn_suma.place(x=90, y=130, width=100, height=30)

        self.btn_resta = tk.Button(root, text="-", command=self.restar)
        self.btn_resta.place(x=210, y=130, width=100, height=30) 

        self.btn_multiplicacion = tk.Button(root, text="*", command=self.multiplicar)
        self.btn_multiplicacion.place(x=90, y=180, width=100, height=30) 

        self.btn_division = tk.Button(root, text="/", command=self.dividir)
        self.btn_division.place(x=210, y=180, width=100, height=30) 

        self.btn_modulo = tk.Button(root, text="%", command=self.calcular_modulo)
        self.btn_modulo.place(x=90, y=230, width=100, height=30)

        self.btn_reset = tk.Button(root, text="CLEAR", command=self.reset)
        self.btn_reset.place(x=210, y=230, width=100, height=30) 

    def sumar(self):
        try:
            num1 = float(self.primer_numero.get())
            num2 = float(self.segundo_numero.get())
            resultado = num1 + num2
            self.resultado.set(resultado)
        except ValueError:
            self.resultado.set("Error")

    def restar(self):
        try:
            num1 = float(self.primer_numero.get())
            num2 = float(self.segundo_numero.get())
            resultado = num1 - num2
            self.resultado.set(resultado)
        except ValueError:
            self.resultado.set("Error")

    def multiplicar(self):
        try:
            num1 = float(self.primer_numero.get())
            num2 = float(self.segundo_numero.get())
            resultado = num1 * num2
            self.resultado.set(resultado)
        except ValueError:
            self.resultado.set("Error")

    def dividir(self):
        try:
            num1 = float(self.primer_numero.get())
            num2 = float(self.segundo_numero.get())
            if num2 == 0:
                self.resultado.set("Error: División por cero")
            else:
                resultado = num1 / num2
                self.resultado.set(resultado)
        except ValueError:
            self.resultado.set("Error")

    def calcular_modulo(self):
        try:
            num1 = float(self.primer_numero.get())
            num2 = float(self.segundo_numero.get())
            if num2 == 0:
                self.resultado.set("Error: División por cero")
            else:
                resultado = num1 % num2
                self.resultado.set(resultado)
        except ValueError:
            self.resultado.set("Error")

    def reset(self):
        self.primer_numero.set("")
        self.segundo_numero.set("")
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x350')
    app = Calculadora(root)
    
    root.mainloop()