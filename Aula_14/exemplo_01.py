from tkinter import *


root = Tk()
root.geometry("512x512")
c = Canvas(root, width=512, height=512)
c.pack()
o = c.create_oval(1, 1, 200, 100, outline="blue", width=5, fill="red")
widget = Button(text="Tk Canvas")
w = c.create_window(10, 120, window=widget, anchor=W)
l = c.create_line(100, 0, 120, 30, 50, 60, 100, 120, fill="black", width=2)
r = c.create_rectangle(40, 150, 100, 200, fill="white")
img = PhotoImage(file="python.gif")
i = c.create_image(150, 150, image=img, anchor=NW)
a = c.create_arc(150, 90, 250, 190, start=30, extent=60, \
                 outline="green", fill="orange")
t = c.create_text(200, 135, text="Texto\nTexto\n", font="Arial 22")
mainloop()
