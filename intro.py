from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('400x400')  # Primero ancho despues largo

# Primero donde renderizo, despues cual es el texto a mostrar
label = Label(root, text='Hola mundo!')
label2 = Label(root, text='Chao mundo!')
# label.pack()  # Muestra los elementos

label.grid(row=0, column=0)
label2.grid(row=0, column=1)

root.mainloop()
