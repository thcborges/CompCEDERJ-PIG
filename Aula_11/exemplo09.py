from tkinter import *
top = Frame(); top.pack(fill='both', expand=True)
f = Frame(top); f.pack(fill='x')
a = Label(f, text="A")
b = Label(f, text="B")
c = Label(f, text="C")
d = Label(top, text="D")

for w in (a, b, c, d):
    w.configure(relief='groove', border=10, font='Times 24 bold')
    w.pack(side='left', expand=True, fill='both')

top.mainloop()
