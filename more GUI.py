from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.btn1=Button(self, text="Nothing !")
        self.btn1.grid()

        self.btn2=Button(self)
        self.btn2.grid()
        self.btn2.configure(text="me too !")

        self.btn3=Button(self)
        self.btn3.grid()
        self.btn3["text"]="Same"
root=Tk()
root.title("lazy Buttons 2")
root.geometry("200x85")
app=Application(root)
root.mainloop()