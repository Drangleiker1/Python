from tkinter import *

window = Tk()

window.maxsize(640,400)
window.minsize(640,400)

photo=PhotoImage(file="Cornwall Cav.png")

label1 = Frame(window, width = 640, height = 400, bd=3,bg="black")
mainFrame = Label(window, text="Witam", font = ("Arial", 24), bd=10, bg="black", fg ="white", image=photo, compound="top")

mainFrame.pack()
window.mainloop()
