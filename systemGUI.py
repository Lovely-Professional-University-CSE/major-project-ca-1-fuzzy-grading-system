
from tkinter import *

window = Tk()
window.title("Student Grading System")
window.geometry("500x500")

global username
global password
username = StringVar()
password = StringVar()

Label(window, text = "Enter username and password below", bg="black",fg="green", font=("calibri", 11)).pack()
Label(window, text = "").pack()

Label(window, text = "Login Id ").pack()
e1 = Entry(window, textvariable=username).pack()

Label(window, text = "Password ").pack()
e2 = Entry(window, textvariable=password, show='*').pack()

Label(window, text="").pack()
Button(window, text="Login", width=10, height=1).pack()


window.mainloop()
