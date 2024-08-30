import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign In Page")
root.geometry('550x350')

# For menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

# Welcome label
w = Label(root, text="Welcome to our Sign in Page", bg="lightgray", fg="black", font=("Helvetica", 16))
w.grid(row=0, column=0, columnspan=4, pady=10)

# Labels and entry fields for first and last name
Label(root, text="First Name :", bg="white", fg="black").grid(row=2, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Last Name :", bg="white", fg="black").grid(row=3, column=0, padx=10, pady=5, sticky=E)

entry1 = Entry(root, selectbackground="lightblue", selectforeground="black", bg="white", fg="black")
entry2 = Entry(root, selectbackground="lightblue", selectforeground="black", bg="white", fg="black")

entry1.grid(row=2, column=1, padx=10, pady=5)
entry2.grid(row=3, column=1, padx=10, pady=5)

# Label and radio buttons for gender
Label(root, text="Gender :", bg="white", fg="black").grid(row=5, column=0, padx=10, pady=5, sticky=E)
cb = IntVar()
Radiobutton(root, text="Male", variable=cb, value=1, bg="white", fg="black").grid(row=5, column=1, sticky=W)
Radiobutton(root, text="Female", variable=cb, value=2, bg="white", fg="black").grid(row=5, column=2, sticky=W)

# Label & radio buttons for programming preference
Label(root, text="Do You Like Programming :", bg="white", fg="black").grid(row=7, column=0, padx=10, pady=5, sticky=E)
var = IntVar()
Radiobutton(root, text="YES", variable=var, value=1, bg="white", fg="black").grid(row=7, column=1, sticky=W)
Radiobutton(root, text="NO", variable=var, value=2, bg="white", fg="black").grid(row=7, column=2, sticky=W)

# For check buttons
Label(root, text="Choose Your Favorite Language :", bg="white", fg="black").grid(row=9, column=0, padx=10, pady=5, sticky=E)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
Checkbutton(root, text="Python", variable=var1, bg="white", fg="black").grid(row=9, column=1, sticky=W)
Checkbutton(root, text="JavaScript", variable=var2, bg="white", fg="black").grid(row=9, column=2, sticky=W)
Checkbutton(root, text="HTML & CSS", variable=var3, bg="white", fg="black").grid(row=11, column=1, sticky=W)
Checkbutton(root, text="Other", variable=var4, bg="white", fg="black").grid(row=11, column=2, sticky=W)

# Combo box
Label(root, text="Your Current Status :", bg="white", fg="black").grid(row=13, column=0, padx=10, pady=5, sticky=E)

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item, bg="white", fg="black")

# Create a label
label = Label(root, text="Selected Item: ", bg="white", fg="black")
label.grid(row=13, column=2, sticky=W, padx=10, pady=5)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Select", "School Student", "College Student", "Service Man"])
combo_box.grid(row=13, column=1, sticky=W, padx=10, pady=5)

# Set default value
combo_box.set("Select")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)

# Define the submit function
def submit():
    first_name = entry1.get()
    last_name = entry2.get()
    gender = "Male" if cb.get() == 1 else "Female"
    programming_preference = "Yes" if var.get() == 1 else "No"
    favorite_languages = []
    if var1.get() == 1:
        favorite_languages.append("Python")
    if var2.get() == 1:
        favorite_languages.append("JavaScript")
    if var3.get() == 1:
        favorite_languages.append("HTML & CSS")
    if var4.get() == 1:
        favorite_languages.append("Other")
    current_status = combo_box.get()
    
    # You can add any action you want to perform with the collected data
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Gender: {gender}")
    print(f"Do You Like Programming: {programming_preference}")
    print(f"Favorite Languages: {', '.join(favorite_languages)}")
    print(f"Current Status: {current_status}")

# Add the submit button
Button(root, text="Submit", command=submit, activebackground="green", activeforeground="black", bg="lightgray", fg="black", font=("arial", 12)).grid(row=17, column=1, padx=10, pady=5, sticky=E)

# Set background color for the root window
root.configure(bg="white")

root.mainloop()
