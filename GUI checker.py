from tkinter import *
class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose your fav movie").grid(row=0, column=0, sticky=W)
        Label(self, text="Select all that apply-").grid(row=1, column=0, sticky=W)
        self.com=BooleanVar()
        Checkbutton(self, text="Comedy", variable=self.com,command=self.update_text).grid(row=2, column=0, sticky=W)
        self.dram = BooleanVar()
        Checkbutton(self, text="Drama", variable=self.dram, command=self.update_text).grid(row=3, column=0, sticky=W)
        self.rom = BooleanVar()
        Checkbutton(self, text="Romance", variable=self.rom, command=self.update_text).grid(row=4, column=0, sticky=W)
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.com.get():
            likes+="Comedy\n"
        if self.dram.get():
            likes+="Drama\n"
        if self.rom.get():
            likes+="romance\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

root=Tk()
root.title("Movie Choose")
app = App(root)
root.mainloop()
