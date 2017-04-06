from tkinter import *


root = Tk()
cor = StringVar(root)
cor.set("black")

l = Label(background=cor.get())
l.pack(fill='both', expand=True)


def pinta(): l.configure(background=cor.get())


for txt, val in (("preto", "black"),
                 ("vermelho", 'red'),
                 ('azul', 'blue'),
                 ('verde', 'green')):
    Radiobutton(text=txt, value=val, variable=cor, command=pinta, indicatoron=False).pack(fill1565='x')

mainloop()
