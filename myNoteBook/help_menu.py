from tkinter import *
from tkinter.messagebox import *
import sys
import time



class Help():
    def about(root):
        full_date=time.localtime()
        year=str(full_date.tm_year)
        showinfo(title="About",message="This is as it look like 'simple text editor' but it save the file in hashed form like password so no one can read it.\n This app is disgned by kibrom Hailu and for education purpose only.\ncopyright "+year+"@All Rights Reserved ")
        
def main(root,text,menubar):
    help=Help()
    
    helpMenu=Menu(menubar, bg="RoyalBlue2",fg="white",tearoff=False)
    helpMenu.add_command(label="About",command=help.about)
    menubar.add_cascade(label="Help",menu=helpMenu)
    
    root.config(menu=menubar)
    
if __name__=="__main__":
    print("Please run 'main.py'")
    