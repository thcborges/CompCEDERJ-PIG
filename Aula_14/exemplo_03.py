from tkinter import *


lb = Listbox()
lb.pack(side=LEFT, expand=True, fill="both")
sb = Scrollbar()
sb.pack(side=RIGHT, fill="y")
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
for i in range(100):
    lb.insert(END, i)
mainloop()
