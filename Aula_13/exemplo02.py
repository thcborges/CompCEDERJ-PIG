from tkinter import *


def alo(): print("Alo!")


root = Tk()
menu = Menu(root, tearoff=0)
menu.add_command(label="Alo 1", command=alo)
menu.add_command(label="Alo 2", command=alo)


def popup(e): menu.post(e.x_root, e.y_root)


frame = Frame(root, width=200, height=200)
frame.pack()
frame.bind("<Button-3>", popup)
root.mainloop()
