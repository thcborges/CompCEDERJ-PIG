from tkinter import *


def clica(e):
    txt = "Mouse clicado em\n%d, %d" % (e.x, e.y)
    r.configure(text=txt)


r = Label()
r.pack(expand=True, fill="both")
r.master.geometry("200x200")
r.bind("<Motion>", clica)
mainloop()
