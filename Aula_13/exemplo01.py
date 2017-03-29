from tkinter import  *


def abrir(): print("abrir")


def salvar(): print("salvar")


def ajuda(): print("ajuda")


top = Tk()
principal = Menu(top)
arquivo = Menu(principal)
arquivo.add_command(label="Abrir", command=abrir)
arquivo.add_command(label="Salvar", command=salvar)
principal.add_cascade(label="Arquivo", menu=arquivo)
principal.add_command(label="Ajuda", command=ajuda)
top.configure(menu=principal)
top.mainloop()
