from tkinter import *

root = Tk()
root.title('Checkboxs')

root.geometry('500x500')

var = StringVar()
var.set('Si')

c = Checkbutton(root, text='Checkbox', variable=var,
                onvalue='Si', offvalue='No')
c.pack()


def mostrar():
    l = Label(root, text=var.get())
    l.pack()


btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()
