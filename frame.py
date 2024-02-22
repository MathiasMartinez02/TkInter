from tkinter import *

root = Tk()
root.title('Hola Mundo')

# borderwidth -> ancho del marco
frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)  # pad = padding

l = Label(frame, text='InFrame')
btn = Button(frame, text='Salir', command=root.quit)  # La ultima cierra la app
l.pack()
btn.pack()
root.mainloop()
