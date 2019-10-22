
from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def login():
    global imglabel
    global username
    global password

    imglabel = Tk()
    imglabel.title("Student Grading System")

    imglabel.configure(background='light blue')
    bg_image = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_image)
    img = Label(imglabel, image = image)
    img.image = image
    img.pack(fill='both', expand=True)
    imglabel.geometry("600x400")
    large_font = ('Verdana',20)

    username = StringVar()
    password = StringVar()

    Label(img, text = "Enter username and password below",fg="black", font=large_font, fill=None).place(y=50, x=50)

    Label(img, text = "Login Id ",bg="light pink", padx=10, pady=10).place(y=100,x=40)
    e1 = Entry(img, textvariable=username,font=large_font).place(y=100,x=120)

    Label(img, text = "Password ",bg="light pink",padx=10, pady=10).place(y=200,x=40)
    e2 = Entry(img, textvariable=password, show='*',font=large_font).place(y=200,x=120)

    Button(img, text="Register",command=register, width=10, height=1, padx=5, pady=5).place(y=280,x=120)
    Button(img, text="Login",command=verify, width=10, height=1, padx=5, pady=5).place(y=280,x=300)

    imglabel.mainloop()

def verify():
    pass

def register():
    database()
    global newname
    global newpass
    imglabel.destroy()
    regt = Tk()
    regt.title("Sign Up")
    regt.geometry("600x400")
    
    regt.mainloop()


def database():
    global conn, cursor
    conn = sqlite3.connect("studentDetails.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'studentInfo' (student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO 'studentInfo' (username, password) VALUES('admin', 'admin')")
        conn.commit()


def deleteUser():
    pass

login()