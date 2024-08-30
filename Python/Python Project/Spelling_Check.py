import tkinter as tk
from textblob import TextBlob

root = tk.Tk()
root.title("Spelling Checker")
root.geometry('700x400')
root.config(bg='#dae6f6')

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())
    spell.config(text=f"Correct text is: {right}")

heading = tk.Label(root, text="Spelling Checker", font=('Trebuchet MS', 30, 'bold'), bg='#dae6f6', fg='#364971')
heading.pack(pady=(50, 0))

enter_text = tk.Entry(root, justify='center', width=30, font=('poppins', 25), bg='white')
enter_text.pack(pady=(30, 0))
enter_text.focus()

button = tk.Button(root, text="Check", font=('arial', 20, 'bold'), fg='white', bg='grey', command=check_spelling)
button.pack(pady=(30, 0))

spell = tk.Label(root, font=('poppins', 20), bg='#dae6f6', fg='#364971')
spell.pack(pady=(50, 0))

root.mainloop()
