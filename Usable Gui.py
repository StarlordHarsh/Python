from tkinter import *

class Appli(Frame):
    def __init__(self, master):
        super(Appli, self).__init__(master)
        self.grid()
        self.btn_clk=0
        self.create_widget()

    def create_widget(self):
        self.btn=Button(self)
        self.btn1=Button(self)
        self.btn["text"]="click:0"
        self.btn1["text"]="Click:0"
        self.btn["command"] = self.update_count
        self.btn1["command"] = self.update_count
        self.btn.grid()
        self.btn1.grid()
        
    def update_count(self):
        self.btn_clk+=1
        self.btn["text"] = "Total Clicks: "+str(self.btn_clk)
        self.btn1["text"] = "Total Clicks: " + str(self.btn_clk)

root=Tk()
root.title("Click Counter")
root.geometry("200x50")
app=Appli(root)
root.mainloop()
