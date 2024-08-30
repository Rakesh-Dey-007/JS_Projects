from tkinter import *
from tkcalendar import *

root = Tk()

# Create a global variable for the selected date label
selectedDate = None

def select_date():
    global selectedDate
    myDate = myCal.get_date()
    if selectedDate:
        selectedDate.config(text=myDate)  # Update the label text if it already exists
    else:
        selectedDate = Label(root, text=myDate, bg="lightblue")
        selectedDate.pack(padx=2, pady=2)

myCal = Calendar(root, setmode="day", date_pattern="d/m/yy")
myCal.pack(padx=15, pady=15)

open_cal = Button(root, text="Select Date", command=select_date)
open_cal.pack(pady=15, padx=15)

root.geometry("300x300")
root.title("Calendar")
root.configure(bg="lightblue")

root.mainloop()
