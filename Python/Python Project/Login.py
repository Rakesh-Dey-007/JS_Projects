from tkinter import *
from tkinter import messagebox
import tkinter as tk

# Create the main window --->
root = Tk()
root.title("Login")
root.geometry("925x450")
root.configure(bg="white")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    if username == 'Rakesh' and password == 'RD_0987':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x450")
        screen.configure(bg="white")

        Label(screen, text="Hello Admin, RD!", bg='#fff', font=('calibri(Body)',50)).pack(expand=True)

        screen.mainloop()
    
    elif username != 'Rakesh' and password != 'RD_0987':
        messagebox.showerror("Error", "Invalid username or password")
    elif password != "Rd_0987":
        messagebox.showerror("Error", "Invalid password")
    elif username != "Rakesh":
        messagebox.showerror("Error", "Invalid username")



# Load the image using a relative path --->
img = PhotoImage(file="Images/Login.png")  # Ensure the image is in the same directory as the script

# Add the image to the window
Label(root, image=img, bg='white').place(x=100, y=120)

frame = Frame(root,width=350,height=350, bg='white')
frame.place(x=450,y=70)

# For Sign in Heading --->
heading = Label(frame,text='Sign in', fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light',24,'bold'))
heading.place(x=100, y=5)


# on_enter & on_leave function --->
def on_enter(e):
    user.delete(0, 'end')

def  on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username")


def on_enter_pass(e):
    code.delete(0, 'end')

def  on_leave_pass(e):
    password = code.get()
    if password == "":
        code.insert(0, "Password")


# For Username Placeholder --->
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',12))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# For Password Placeholder --->
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',12))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_pass)
code.bind('<FocusOut>', on_leave_pass)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


# For Button --->
Button(frame, text='Sign In', width=39, pady=7, bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame,text="Don't have an account?", fg="black", bg="white",font=('Microsoft YaHei UI Light',10)).place(x=75, y=270)

sign_up = Button(frame,width=6,text='Sign in',border=0, fg="#57a1f8", bg="white",cursor='hand2').place(x=215, y=270)


# Run the main event loop --->
root.mainloop()
