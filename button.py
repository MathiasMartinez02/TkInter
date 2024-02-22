from tkinter import *

root = Tk()
root.title('Hola Mundo')

l = Label(root, text='Hola mundo')


def click():
    l.pack()


# (Donde se muestra, texto, funcion, color del texto, fondo del boton)
btn = Button(root, text='Clickeame', command=click, fg='red', bg='gray')
btn.pack()

root.mainloop()
