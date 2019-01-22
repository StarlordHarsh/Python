from tkinter import *
root=Tk()
root.title("Label")
root.geometry("200x100")
app=Frame(root)
app.grid()
lbl = Label(app, text = "This a label !")
lbl.grid()
root.mainloop()
