from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Notepad By RD')
root.geometry('500x500')
root.config(bg='lightblue')
root.resizable(False,False)

def save_file():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('text files','*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

button_1 = Button(root, width='20', height='2',bg='#fff',border=0,cursor='hand2', text='Save File', command=save_file).place(x=80,y=10)
button_2 = Button(root, width='20', height='2',bg='#fff',border=0,cursor='hand2',
 text='Open File', command=open_file).place(x=260,y=10)

entry=Text(root, width='43', height='18',font=('arial',15), wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()