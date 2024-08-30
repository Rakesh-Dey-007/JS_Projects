import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()
root = Tk()

def speak_now():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=25,bd=1)
obj.pack(padx=10, pady=10, fill="both", expand="yes")

lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10, border=None, outline=None)

btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speak_now)
btn.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False, False)

root.mainloop()