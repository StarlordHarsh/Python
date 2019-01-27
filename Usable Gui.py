from tkinter import *

class Appli(Frame):

    def __init__(self, master):
        super(Appli, self).__init__(master)
        self.grid()
        self.btn_clk=0
        self.btn_clk1=0
        self.create_widget()

    def create_widget(self):
        self.btn=Button(self)
        self.btn1=Button(self)
        self.btn2=Button(self)
        self.btn["text"]="click:0"
        self.btn1["text"]="Click:0"
        self.btn2["text"] = "Reset"
        self.btn["command"] = self.update_count
        self.btn1["command"] = self.update_count_both
        self.btn2["command"] = self.reset()
        self.btn.grid()
        self.btn1.grid()
        self.btn2.grid()

    def update_count(self):
        self.btn_clk+=1
        self.btn["text"] = "Total Clicks: "+str(self.btn_clk)
        self.btn1["text"] = "Total Clicks: " + str(self.btn_clk1)

    def update_count_both(self):
        self.btn_clk+=1
        self.btn_clk1+=1
        self.btn["text"] = "Total Clicks: "+str(self.btn_clk)
        self.btn1["text"] = "Total Clicks: " + str(self.btn_clk1)

    def reset(self):
        self.btn_clk=0
        self.btn_clk1= 0
        self.btn["text"] = "Total Clicks: " + str(self.btn_clk)
        self.btn1["text"] = "Total Clicks: " + str(self.btn_clk1)

root=Tk()
root.title("Click Counter")
root.geometry("400x100")
app=Appli(root)
root.mainloop()
