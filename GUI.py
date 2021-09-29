from tkinter import *
root = Tk()
root.title ("First GUI")
myText = Label(text="Mynameis",fg="blue",font=20).grid(row=0,column=0)
myText = Label(text="Priscilla",fg="green",font=20).grid(row=1,column=1)
myText = Label(text="Rakarsrom",fg="red",font=20).grid(row=2,column=2)
root.geometry("300x300")
root.mainloop()
