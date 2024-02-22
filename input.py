from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

e = Entry(root, width=45)  # (Donde colocarlo, ancho)
e.pack()
e.insert(0, "Ingrese Texto")


def click():
    texto = e.get()  # Toma el texto en campo de texto
    # l.configure(text=texto)  # Actualiza el Label con el texto anterior
    textvariable.set(texto)
    e.delete(0, END)


textvariable = StringVar()

btn = Button(root, text='click', command=click)
btn.pack()

# l = Label(root, text='Texto de la etiqueta')
# l.pack()

l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()
