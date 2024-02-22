from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview')

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Apellido', 'Telefono', 'Empresa')

tree.column('#0')
tree.column('Nombre')
tree.column('Apellido')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('#0', text='id')
tree.heading('Nombre', text='Nombre')
tree.heading('Apellido', text='Apellido')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', END, '1', values=('Mathias', 'Martinez',
            '123455212', 'Globant'), text='Uno')
tree.insert('', END, '2', values=(
    'Juan', 'Perez', '3425943029', 'ICBC'), text='Dos')
tree.insert('', END, '3', values=(
    'Emiliano', 'Denada', '351202928', 'FIBA'), text='Tres')
tree.insert('1', END, '4', values=(
    'Emma', 'Martinez', '123123123', 'IBM'), text='Hijo')


root.mainloop()
