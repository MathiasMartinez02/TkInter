from tkinter import *

root = Tk()
root.title('Radio Button')

# r = IntVar()
# r.set('1')

# Radiobutton(root, text='Opcion 1', variable=r, value=1).pack()
# Radiobutton(root, text='Opcion 2', variable=r, value=2).pack()

Tuplas = [
    ('Plata', 'O plomo'),
    ('Rayo', 'Cuchau'),
    ('Chipi', 'Chapa'),
    ('Blue', 'Label')
]

tupla = StringVar()
tupla.set('Label')

for text, meme in Tuplas:
    Radiobutton(root, text=text, variable=tupla, value=meme).pack()

l = Label(root, textvariable=tupla)
l.pack()

root.mainloop()
