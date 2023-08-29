import tkinter as tk
from tkinter import ttk

class Peliculas:
    def __init__(self, root):
        self.root = root
        self.root.title("Películas")

        self.label_titulo = tk.Label(root, text="Escribe el título de una película:")
        self.label_titulo.place(x=30, y=100)

        self.lineEdit = tk.Entry(root)
        self.lineEdit.place(x=40, y=130)

        self.label_peli = tk.Label(root, text="Peliculas")
        self.label_peli.place(x=280, y=100)

        self.listWidget = tk.Listbox(root)
        self.listWidget.place(x=250, y=130)

        self.btn_anadir = tk.Button(root, text="Añadir", command=self.anadir_pelicula)
        self.btn_anadir.place(x=80, y=170)

    def anadir_pelicula(self):
        titulo_pelicula = self.lineEdit.get()
        if titulo_pelicula:
            self.listWidget.insert(tk.END, titulo_pelicula)

        self.lineEdit.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x350')
    app = Peliculas(root)
    root.mainloop()
