from tkinter import *


root = Tk()
v1 = IntVar(root)
v2 = StringVar(root)


def exibe():
    l.config(text="v1 = %d, v2 = %s" % (v1.get(), v2.get()))


c1 = Checkbutton(text="V1", var=v1, command=exibe)
c2 = Checkbutton(text="V2", var=v2, command=exibe, onvalue="Sim", offvalue="Não")

l = Label()
for w in (c1, c2, l): w.pack()
exibe()
mainloop()
