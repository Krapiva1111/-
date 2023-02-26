from tkinter import *
from random import *
window = Tk()
canv = Canvas(window,width=300,height=300)
canv.pack()
def fig():
    canv.delete("all")
    a = randint(1,3)
    if a == 1:
        canv.create_rectangle(randint(0,300), randint(0,300), randint(0,300), randint(0,300), fill="yellow")
    elif a == 2:
        canv.create_oval(randint(0,300), randint(0,300), randint(0,300), randint(0,300), fill="blue")
    else:
        canv.create_polygon(randint(0,300), randint(0,300), randint(0,300), randint(0,300), randint(0,300), fill="red")
button = Button(window, text="Нарисовать фигуру", command=fig)
button.pack()
window.mainloop()