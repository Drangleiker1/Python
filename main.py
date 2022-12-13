from tkinter import *
from tkinter import filedialog as fd

def add_image():
    filetypes = (
        ('Obrazki PNG', '*.png'),
        ('All files', '*.*')
    )
    fd.askopenfilename(filetypes=filetypes)

window = Tk()
window.minsize(640, 480)
window.minsize(640, 480)
window.geometry("640x480")

photo = PhotoImage(file="Cornwall Cav.png")

frame1 = Frame(window, bg="black", height= 50)
frame1.pack()

addButton = Button(frame1, command=add_image, text = "Dodaj obrazek", font = ("Arial", 24), )
addButton.pack()

mainLabel= Label(window,
                  text="Moja pierwsza gra",
                  font = ("Arial", 28),
                  bd=10,
                  bg="black",
                  fg="white",
                  image=photo,
                  compound="top")

mainLabel.pack()
window.mainloop()