
from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def login():
    global imglabel
    global username
    global password
    #if 'normal' == regt.state():
    #    regt.destroy()
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
def Back():
    regt.destroy()
    login()

def regback():
    database()
    cursor.execute("INSERT INTO 'studentInfo' (username, password) VALUES(newname, newpass)")
    conn.commit()
    conn.close()
    regt.destroy()
    login()


    
def register():
    
    global newname
    global newpass
    global regt
   
    imglabel.destroy()
    regt = Tk()

    bg_reg = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_reg)
    imgreg = Label(regt, image = image)
    imgreg.image = image
    imgreg.pack(fill='both', expand=True)

    regt.title("Sign Up")
    regt.geometry("600x400")
    
    newname = StringVar()
    newpass = StringVar()
    
    lbl_title = Label(imgreg, text = " Login Application", font=('arial', 15)).place(y=50, x=50)

    lbl_username = Label(imgreg, text = "Username:", font=('arial', 14), padx=10, pady=10).place(y=100,x=40)
    user1 = Entry(imgreg, textvariable=newname, font=('arial', 14)).place(y=100,x=200)

    lbl_password = Label(imgreg, text = "Password:", font=('arial', 14), padx=10, pady=10).place(y=200,x=40)
    passw1 = Entry(imgreg, textvariable=newpass, show="*", font=('arial', 14)).place(y=200,x=200)

    Button(imgreg, text="Back", width=10, command=Back, padx=5, pady=5).place(y=280,x=120)
    Button(imgreg, text="Register", width=10, command=regback, padx=5, pady=5).place(y=280,x=280)
    

    lbl_text = Label(imgreg).place(y=300, x=150)
    

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")

    regt.mainloop()


def database():
    global conn, cursor
    conn = sqlite3.connect("studentDetails.db")
    cursor = conn.cursor()
    #cursor.execute("CREATE TABLE IF NOT EXISTS 'studentInfo' (student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
    
    cursor.execute("SELECT * FROM 'studentInfo'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO 'studentInfo' (username, password) VALUES('admin', 'admin')")
        conn.commit()


def deleteUser():
    pass

login()
