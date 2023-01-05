from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
    global filename
    filename = "untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    with open(filename, "w") as f:
        f.write(t)

def saveAs():
    f = asksaveasfile(mode='w', defaultextextension=".txt")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="oops", message="unable to save file")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


root = Tk()
root.title = "Python-Based text editor"
root.minsize(width=400, height=500)
root.maxsize(width=400, height=500)

text = Text(root, width=400, height=500)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()





