from tkinter import *
top = Frame(); top.pack(fill='both', expand=True)
a = Label(top, text="A"); a.pack(side="left",
                                 expand=True,
                                 fill="both"
                                 )
b = Label(top, text="B"); b.pack(side="bottom",
                                 expand=True,
                                 fill="both"
                                 )
c = Label(top, text="C"); c.pack(side="right")
d = Label(top, text="D"); d.pack(side="top")

a.configure(relief="groove", border=10, font="Timer 24 bold")
b.configure(relief="groove", border=10, font="Timer 24 bold")
c.configure(relief="groove", border=10, font="Timer 24 bold")
d.configure(relief="groove", border=10, font="Timer 24 bold")

# for widget in (a, b, c, d):
#     widget.configure(relief="groove", border=10, font="Timer 24 bold")

top.master.geometry("300x300+200+200")
top.mainloop()
