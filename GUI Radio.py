from tkinter import *
class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose your fav movie").grid(row=0, column=0, sticky=W)
        Label(self, text="Select one that apply-").grid(row=1, column=0, sticky=W)
        self.fav = StringVar()
        self.fav.set(None)

        Radiobutton(self, text="Comedy", variable=self.fav, value="Comedy", command=self.update_text).grid(row=2, column=0, sticky=W)
        Radiobutton(self, text="Romance", variable=self.fav, value="Romance", command=self.update_text).grid(row=2, column=1, sticky=W)
        Radiobutton(self, text="Drama", variable=self.fav, value="Drama", command=self.update_text).grid(row=2, column=2, sticky=W)

        self.results_txt=Text(self, width=40,height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        message="Your fav type movie is-"
        message+=self.fav.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

root=Tk()
root.title("Movi Cohser 2")
app = App(root)

root.mainloop()