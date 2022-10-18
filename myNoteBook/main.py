from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu




















root = Tk()
root.title("Text Encrypter")
root.geometry("800x500")
root.config(bg="gray35")
root.minsize(width=400, height =400)
text=ScrolledText(root,state='normal',width=400,height=200,wrap='word',pady=2,padx=3,undo=True)
text.pack(fill=Y,expand=1)
text.focus_set()
menubar=Menu(root,tearoff=False,background="gray35",fg="white")
file_menu.main(root,text,menubar)
edit_menu.main(root,text,menubar)
format_menu.main(root,text,menubar)
help_menu.main(root,text,menubar)
root.mainloop()
