from tkinter import *
top = Frame(); top.pack()
rotulo = Label(top, text="Rótulo Exemplo", foreground='blue')
rotulo.pack()

rotulo.configure(relief="ridge", font="Arial 24 bold", border=5, background='yellow')

print("rotulo.configure(relief=\"ridge\")\n", rotulo.configure(relief="ridge"))
print("rotulo.configure(\"ridge\")\n", rotulo.configure("relief"))
print("rotulo.configure()['relief']\n", rotulo.configure()['relief'])
print("rotulo.configurerotulo.configure('relief')[4]\n", rotulo.configure('relief')[4])
print("rotulo.configurerotulo.cget('relief')\n", rotulo.cget('relief'))


mainloop()
