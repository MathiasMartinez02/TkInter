from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')


# def click():
#     messagebox.showwarning('Popup', 'Hola mundo!')

# def click():
#     messagebox.showinfo('Popup', 'Hola mundo!')

# def click():
#     messagebox.showerror('Popup', 'Hola mundo!')

# def click():
#     rta = messagebox.askquestion('Popup', 'Hola mundo!')
#     if rta == 'yes':
#         messagebox.showinfo('Respuesta', 'La respuesta fue ' + rta)
#     else:
#         messagebox.showinfo('Respuesta', 'La respuesta fue ' + rta + ' :c')

# def click():
#     rta = messagebox.askokcancel('Hola Mundo', 'Desea realizar accion?')
#     if rta:
#         messagebox.showinfo('Hola Mundo!',  'La respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola Mundo!', 'La respuesta fue Cancelar')

def click():
    rta = messagebox.askyesno('Hola Mundo', 'Desea realizar accion?')
    if rta:
        messagebox.showinfo('Hola Mundo!',  'La respuesta fue Yes')
    else:
        messagebox.showinfo('Hola Mundo!', 'La respuesta fue No')


btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
