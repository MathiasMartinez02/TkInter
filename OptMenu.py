from tkinter import *

root = Tk()
root.title('Option Menu')
root.geometry('500x500')


def enviar():
    l = Label(root, text=value.get())
    l.pack()


list = [
    'Si',
    'No',
    'Nose'
]

value = StringVar()
value.set(list[2])

drop = OptionMenu(root, value, *list)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
