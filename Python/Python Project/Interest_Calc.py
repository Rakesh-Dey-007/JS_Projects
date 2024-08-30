# Simple Interest calculator

from tkinter import *

root=Tk()
root.title("Simple interest calculator")
root.geometry("500x300")

def Calculate():
  principal = int(principalvalue.get())
  rate = float(ratevalue.get())
  time = int(timevalue.get())
  interest = (principal * rate * time) / 100
  result = "The Simple Interest is : " + str(interest)
  Label(root, text=result, font="arial 15").place(x=200, y=250)

principal=Label(root, text="Principal:", font="arial 15")
rate=Label(root, text="Rate of Interest:", font="arial 15")
time=Label(root, text="Time:", font="arial 15")

principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)

principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()

principalentry=Entry(root, textvariable=principalvalue, font="arial 20", width=8)
rateentry=Entry(root, textvariable=ratevalue, font="arial 20", width=8)
timeentry=Entry(root, textvariable=timevalue, font="arial 20", width=8)

principalentry.place(x=200,y=20)
rateentry.place(x=200,y=90)
timeentry.place(x=200,y=160)

Button(text="Calculate", font="arial 15", command=Calculate).place(x=350,y=20)
Button (root, text="Exit", command=lambda:exit(), font="arial 15", width=8).place (x=350,y=90)

root.mainloop()