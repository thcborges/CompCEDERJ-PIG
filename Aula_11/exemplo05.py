from tkinter import *
top = Frame(); top.pack()
a = Label(top, text="A"); a.pack(side="left", fill="y")
b = Label(top, text="B"); b.pack(side="bottom", fill="x")
c = Label(top, text="C"); c.pack(side="right")
d = Label(top, text="D"); d.pack(side="top")

a.configure(relief="groove", border=10, font="Timer 24 bold")
b.configure(relief="groove", border=10, font="Timer 24 bold")
c.configure(relief="groove", border=10, font="Timer 24 bold")
d.configure(relief="groove", border=10, font="Timer 24 bold")

# for widget in (a, b, c, d):
#     widget.configure(relief="groove", border=10, font="Timer 24 bold")

top.mainloop()
