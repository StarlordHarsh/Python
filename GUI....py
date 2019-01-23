from tkinter import *

class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Enter password")
        self.inst_lbl.grid(row=0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky = W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        self.submit_btn = Button(self, text = "Submit", command = self.reveal)
        self.submit_btn.grid(row = 2, column = 0, sticky = W)
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        contents = self.pw_ent.get()
        if(contents == "secret"):
            message = "Here's the secret !"
        else:
            message = "Incorrect Password"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

root=Tk()
root.title("Pass")
root.geometry("400x200")
app=App(root)
root.mainloop()