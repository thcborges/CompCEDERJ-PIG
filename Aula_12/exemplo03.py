from tkinter import *


def clica(e):
    txt = "Mouse clicado em\n%d, %d" % (e.x, e.y)
    r.configure(text=txt)
    r.focus()


def tecla(e):
    txt = "Keysym = %s\nKeycode = %s\nChar = %s" % (e.keysym, e.keycode, e.char)
    r.configure(text=txt)


r = Label()
r.pack(expand=True, fill="both")
r.master.geometry("200x200")
r.bind("<Button-1>", clica)
r.bind("<Key>", tecla)
mainloop()
