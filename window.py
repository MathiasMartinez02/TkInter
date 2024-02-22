from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Window')


def open():
    img = ImageTk.PhotoImage(Image.open('images/cascada.png'))
    top = Toplevel()
    top.title('Nueva Ventana')
    l = Label(top, text='Titulo de la Imagen')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()


btn = Button(root, text='Click', command=open).pack()

root.mainloop()
