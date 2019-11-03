from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from login_signUp import *
from login_signUp import regnologin
from fuzzySystem import fuzzy_logics

def basewindow():
    
    home = Tk()

    database()
    cursor.execute("SELECT * FROM studentInfo WHERE student_id=?", (str(regnologin.get()),))
    det = cursor.fetchone()

    bg_home = Image.open("GPA11.png")
    image = ImageTk.PhotoImage(bg_home)
    imghome = Label(home, image = image)
    imghome.image = image
    imghome.pack(fill='both', expand=True)

    home.title("Grading System")
    home.geometry("600x400")
    
    Label(imghome, text = f"Hello, {det[1]}",fg="black", font=('arial', 14), fill=None).place(y=50, x=50)
    Label(imghome, text = "Fill subject marks to find CGPA",fg="black", font=('arial', 14), fill=None).place(y=100, x=50)

    Button(imghome, text="Maths",command=lambda: inputmarks("Maths",0), width=10, height=1, padx=5, pady=5).place(y=150,x=100)
    Button(imghome, text="English",command=lambda: inputmarks("English",1), width=10, height=1, padx=5, pady=5).place(y=150,x=240)
    Button(imghome, text="Chemistry",command=lambda: inputmarks("Chemistry",2), width=10, height=1, padx=5, pady=5).place(y=200,x=100)
    Button(imghome, text="Physics",command=lambda: inputmarks("Physics",3), width=10, height=1, padx=5, pady=5).place(y=200,x=240)
    Button(imghome, text="Optional",command=lambda: inputmarks("Optional",4), width=10, height=1, padx=5, pady=5).place(y=250,x=100)

    Button(imghome, text="Find CGPA",command=result, width=20, height=2).place(y=280,x=350)
    

    home.mainloop()


def marksdatabase():
    global conn1, cursor1
    conn1 = sqlite3.connect("studentDetails.db")
    cursor1 = conn1.cursor()
    cursor1.execute("CREATE TABLE IF NOT EXISTS 'studentMarks' (student_id TEXT NOT NULL PRIMARY KEY, maths TEXT, physics TEXT, chemistry TEXT, english TEXT, optional TEXT)")

def marksdata():
    marksdatabase()
    param = (str(regnologin), str(sum(mat)//5), str(sum(phy)//5), str(sum(che)//5), str(sum(eng)//5), str(sum(opt)//5))
    cursor.execute("INSERT INTO 'studentInfo' (student_id, maths, physics, chemistry, english, optional) VALUES(?,?,?,?,?,?)", param)
    conn1.commit()
    conn1.close()

def result():
    pass


def collect(subjct, atten, final, hal, ca, pos):

    

    global mat = [0,0,0,0]
    global phy = [0,0,0,0]
    global che = [0,0,0,0]
    global eng = [0,0,0,0]
    global opt = [0,0,0,0]

    if(subjct=="Maths"):
        mat = [ca, atten, hal, final]

    elif(subjct=="English"):
        eng = [ca, atten, hal, final]

    elif(subjct=="Chemistry"):
        che = [ca, atten, hal, final]

    elif(subjct=="Physics"):
        phy = [ca, atten, hal, final]

    elif(subjct=="Optional"):
        opt = [ca, atten, hal, final]

    inp.destroy()


def inputmarks(subjects, pos):
    
    global att, fin, half, clas

    marksdatabase()

    att = StringVar()
    fin = StringVar()
    half = StringVar()
    clas = StringVar()
    global inp

    inp = Tk()

    inp.title(subjects)
    inp.geometry("600x400")

    Label(inp, text = "Enter Marks",fg="black", font=('arial', 14), fill=None).place(y=30, x=50)

    Label(inp, text = "Class Test ",bg="light pink", font=('arial', 14)).place(y=80,x=40)
    Entry(inp, textvariable=clas, font=('arial', 14)).place(y=80,x=180)

    Label(inp, text = "Attendance ",bg="light pink", font=('arial', 14)).place(y=140,x=40)
    Entry(inp, textvariable=att, font=('arial', 14)).place(y=140,x=180)

    Label(inp, text = "Half Term ",bg="light pink", font=('arial', 14)).place(y=200,x=40)
    Entry(inp, textvariable=half, font=('arial', 14)).place(y=200,x=180)

    Label(inp, text = "Final Term ",bg="light pink", font=('arial', 14)).place(y=260,x=40)
    Entry(inp, textvariable=fin, font=('arial', 14)).place(y=260,x=180)

    Button(inp, text="Submit",command=lambda: collect(subjects, int(att), int(fin), int(half), int(clas), pos), width=20, height=2).place(y=320,x=300)

    inp.mainloop()

basewindow()