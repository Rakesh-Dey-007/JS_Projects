import tkinter as tk
from time import strftime

root = tk.Tk()
# root.geometry("700x400")
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('arial', 50, 'bold'), background='black', foreground='grey')
label.pack(anchor='center')

time()
root.mainloop()