from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from login_signUp import *
from login_signUp import regnologin

def basewindow():
    print(regnologin)
    home = Tk()

    database()
    cursor.execute("SELECT * FROM studentInfo WHERE student_id=?", (str(regnologin.get()),))
    det = cursor.fetchone()

    bg_home = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_home)
    imghome = Label(home, image = image)
    imghome.image = image
    imghome.pack(fill='both', expand=True)

    home.title("Home Window")
    home.geometry("800x600")
    
    Label(imghome, text = f"Hello, {det[1]}",fg="black", font=('arial', 14), fill=None).place(y=50, x=50)

    home.mainloop()


def marksdatabase():
    global conn1, cursor1
    conn1 = sqlite3.connect("studentDetails.db")
    cursor1 = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'studentMarks' (student_id TEXT NOT NULL PRIMARY KEY, username TEXT, password TEXT)")

basewindow()

