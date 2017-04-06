from tkinter import *


master = Tk()
c = Canvas(master, width=512, height=512)
c.pack()


def novalinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    c.create_line(x, y, x, y, tags="corrente")


def estendelinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    coords = c.coords("corrente") + [x, y]
    c.coords("corrente", *coords)


def fechalinha(e):
    c.itemconfig("corrente", tags=())


def selecionalinha(e):
    global x0, y0
    x0, y0 = c.canvasx(e.x), c.canvasy(e.y)
    c.itemconfig(CURRENT, tags="sel")


def movelinha(e):
    global x0, y0
    x1, y1 = c.canvasx(e.x), c.canvasy(e.y)
    c.move("sel", x1 - x0, y1 - y0)
    x0, y0 = x1, y1


def deselecionalinha(e):
    c.itemconfig("sel", tags=())


c.bind("<Button-1>", novalinha)
c.bind("<B1-Motion>", estendelinha)
c.bind("<ButtonRelease-1>", fechalinha)
c.bind("<Button-3>", selecionalinha)
c.bind("<B3-Motion>", movelinha)
c.bind("<ButtonRelease-3>", deselecionalinha)
c.pack()
mainloop()
