import tkinter as tk
from tkinter import filedialog
import pyautogui

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def Take_Screenshot():
    screenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        screenshot.save(file_path)

button = tk.Button(text="Take Screenshot", bg="black", fg="white", command=Take_Screenshot)
canvas.create_window(150, 150, window=button)

root.mainloop()
