from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Hola Mundo!')

# imagen = Image.open('cascada.jpg')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('images/cascada.png'))
l = Label(image=img)
l.pack()

root.mainloop()
