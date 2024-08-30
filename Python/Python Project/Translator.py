from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

root = Tk()
root.title("Google Translator 7.0")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(bg="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    translator = GoogleTranslator(source=combo1.get().lower(), target=combo2.get().lower())
    trans_text = translator.translate(text_)

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# Provide the correct path to your images
image_icon = PhotoImage(file="images/Login.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="images/arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

language = GoogleTranslator().get_supported_languages(as_dict=True)
languageV = list(language.values())

# First Combobox --->
combo1 = ttk.Combobox(root, values=languageV, font=("Roboto", 14), state='readonly')
combo1.place(x=110, y=20)
combo1.set('English')

label1 = Label(root, text='English', font=("Segoe", 30, "bold"), bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# 2nd Combobox --->
combo2 = ttk.Combobox(root, values=languageV, font=("Roboto", 14), state='readonly')
combo2.place(x=730, y=20)
combo2.set('Select Language')

label2 = Label(root, text='English', font=("Segoe", 30, "bold"), bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# First frame --->
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font=("Roboto", 20), bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side='right', fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# 2nd frame --->
f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font=("Roboto", 20), bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side='right', fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button --->
translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=476, y=250)

label_change()
root.mainloop()
