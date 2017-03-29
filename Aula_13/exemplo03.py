from tkinter import *


root = Tk()

soma = DoubleVar(root)
parcela = DoubleVar(root)


def aritmetica(e):
    soma.set(soma.get() + parcela.get())


lsoma = Label(textvar=soma)
eparcela = Entry(textvar=parcela)
eparcela.bind("<Return>", aritmetica)
lsoma.pack()
eparcela.pack()
root.mainloop()
