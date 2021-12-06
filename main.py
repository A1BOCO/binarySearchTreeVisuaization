
import tkinter
from tkinter import messagebox

from binaryTree import BinaryTree




diameter = 100
radius = diameter /2
fontSize = 30

CANVASHEIGHT = 1000
CANVASWIDTH = 1800




def add_node():
    entrytext = entry.get()
    if entrytext[0] =="[" and entrytext[-1] == "]":
        entrytext = eval(entrytext)
    if isinstance(entrytext, str):

        message = binarytree.addNode(int(entrytext))
        if message is not None:
            messagebox.showinfo('message',message)
    elif isinstance(entrytext, list):
        for value in entrytext:
            binarytree.addNode(value)


def delete_node():
    entrytext = entry.get()
    message = binarytree.delete_node(int(entrytext))
    if message is not None:
        messagebox.showinfo('message', message)

def clear_canvas():
    binarytree.clear()
    canvas.delete("all")










root = tkinter.Tk()
root.title("Binary Tree")
root.geometry('1800x1000')
root.resizable(0,0)

canvas = tkinter.Canvas(root, bg="white", height=CANVASHEIGHT, width=CANVASWIDTH)
binarytree = BinaryTree(canvas)
frame_top = tkinter.LabelFrame(root,bg='lightgray',text='controller')
frame_top.grid(column=0, row=1,sticky=tkinter.NSEW)
button1 = tkinter.Button(frame_top, text='add node',command=add_node)
button1.grid(row=1, column=2)

button2 = tkinter.Button(frame_top, text='delete node',command=delete_node)
button2.grid(row=1, column=5)

button_clear = tkinter.Button(frame_top, text='Clear Canvas',command=clear_canvas)
button_clear.grid(row=1, column=6)

label = tkinter.Label(frame_top,text="Number")
label.grid(row=1,column=0)
label_random = tkinter.Label(frame_top,text="Number")
label_random.grid(row=0,column=0)



entry = tkinter.Entry(frame_top)
entry.grid(row=1, column=1)


canvas.grid()
root.mainloop()

