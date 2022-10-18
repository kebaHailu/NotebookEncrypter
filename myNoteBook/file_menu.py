from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from cryptography.fernet import Fernet
import sys

class File():
    def newFile(self):
        self.filename="untitled"
        self.text.delete(0.0,END)
        
    def saveFile(self):
        try:
            t=self.text.get(0.0,END)
            f=open(self.filename,'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()
   
    def saveAs(self):
        f=asksaveasfile(mode='w',defaultextension='.txt')
        t=self.text.get(0.0,END)
        key = Fernet.generate_key()
        fernet = Fernet(key)
        e = fernet.encrypt(t.encode())
        t=key.decode() + e.decode()
        
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Oops!",message="Unable to save file...")
    def openFile(self):
        try:
            f=askopenfile(mode='r')
            self.filename=f.name
            t=f.read()
            newKey=t[0:44]
            newWord=t[44:]
        
            fer = Fernet(newKey)
            newDec=fer.decrypt(newWord.encode()).decode() 
            t=newDec
            self.text.delete(0.0,END)
            self.text.insert(0.0,t)
        except:
            showerror(title="Oops!",message="the file you are trying to open is not encrypted. use other text file editer")
    def quit(self):
        entry=askyesno(title="Quit",message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()
    def __init__(self,text,root):
        self.filename = None
        self.text = text
        self.root = root
        
def main(root,text,menubar):
    filemenu = Menu(menubar,bg="RoyalBlue2",fg="white",tearoff=False)
    objFile = File(text,root)
    filemenu.add_command(label="New",command=objFile.newFile)
    filemenu.add_command(label="Open",command=objFile.openFile)
    filemenu.add_command(label="Encrypt",command=objFile.saveFile)
    filemenu.add_command(label="Encrypt As...",command=objFile.saveAs)
    
    filemenu.add_separator()
    filemenu.add_command(label="Quit",command=objFile.quit)
    menubar.add_cascade(label="File",menu=filemenu)
    root.config(menu=menubar)
if __name__ == "__main__":
    print("please run 'main.py'")
        
    
                     
