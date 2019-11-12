# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:50:48 2019

@author: srika
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:19:22 2019

@author: admin
"""

from tkinter import *
import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
   
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    global var1
    var1=StringVar()
    global var2
    global variable1
    global variable2
    var2=StringVar()
    global var3
    var3=StringVar()
    
    global variable3
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("350x300")

    Label(login_success_screen, text="input for mte(0-70)").pack()
    variable1 = Entry(login_success_screen, textvariable=var1)
    variable1.pack()
    Label(login_success_screen, text="input for ete(0-40)").pack()
    variable2 = Entry(login_success_screen, textvariable=var2)
    variable2.pack()

    Label(login_success_screen, text="input for att(0-5)").pack()
    variable3 = Entry(login_success_screen, textvariable=var3)
    variable3.pack()

    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=origin).pack()
    '''Button(login_success_screen, text="OK", command=delete_login_success).pack()
 '''
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def origin():


   import numpy as np
   import skfuzzy as fuzz
   from skfuzzy import control as ctrl
   
   mte=ctrl.Antecedent(np.arange(0,41,1),'mte')
   ete=ctrl.Antecedent(np.arange(0,71,1),'ete')
   att=ctrl.Antecedent(np.arange(0,6,1),'att')
   grade=ctrl.Consequent(np.arange(0,11,1),'grade')
   mte['l']=fuzz.trimf(mte.universe, [0,15,25])
   mte['m']=fuzz.trimf(mte.universe, [15,25,30])
   mte['h']=fuzz.trimf(mte.universe, [25,30,40])
   ete['l']=fuzz.trimf(ete.universe, [0,20,35])
   ete['m']=fuzz.trimf(ete.universe, [20,35,45])
   ete['h']=fuzz.trimf(ete.universe, [35,45,70])
   att['l']=fuzz.trimf(att.universe, [0,2,3])
   att['m']=fuzz.trimf(att.universe, [2,3,4])
   att['h']=fuzz.trimf(att.universe, [3,4,5])
   grade['l']=fuzz.trimf(grade.universe,[0,2,6])
   grade['m']=fuzz.trimf(grade.universe,[2,6,8])
   grade['h']=fuzz.trimf(grade.universe,[6,8,10])
   mte.view()
   ete.view()
   att.view()
   rule1=ctrl.Rule(mte['l'] | ete['l'] | att['l'],grade['l'])
   rule2=ctrl.Rule(mte['m'] | ete['l'] | att['l'],grade['l'])
   rule3=ctrl.Rule(mte['l'] | ete['m'] | att['l'],grade['l'])
   rule4=ctrl.Rule(mte['l'] | ete['l'] | att['m'],grade['l'])
   rule5=ctrl.Rule(mte['l'] | ete['l'] | att['h'],grade['l'])
   rule6=ctrl.Rule(mte['l'] | ete['h'] | att['l'],grade['m'])
   rule7=ctrl.Rule(mte['h'] | ete['l'] | att['l'],grade['m'])
   rule8=ctrl.Rule(mte['l'] | ete['l'] | att['h'],grade['l'])
   rule9=ctrl.Rule(mte['m'] | ete['m'] | att['l'],grade['m'])
   rule10=ctrl.Rule(mte['m'] | ete['l'] | att['m'],grade['l'])
   rule11=ctrl.Rule(mte['l'] | ete['m'] | att['m'],grade['m'])
   rule12=ctrl.Rule(mte['m'] | ete['m'] | att['m'],grade['m'])
   rule13=ctrl.Rule(mte['h'] | ete['h'] | att['l'],grade['h'])
   rule14=ctrl.Rule(mte['h'] | ete['h'] | att['h'],grade['h'])
   rule15=ctrl.Rule(mte['l'] | ete['h'] | att['h'],grade['h'])
   rule16=ctrl.Rule(mte['h'] | ete['l'] | att['h'],grade['m'])
   wm_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule16])
   wm=ctrl.ControlSystemSimulation(wm_ctrl)
   set1=[]
   set1=var1.get()
   set2= var2.get()
   set3= var3.get()
   wm.input['mte']= set1
   wm.input['ete']= set2
   wm.input['att']= set3
   wm.compute()
   print(wm.output['grade'])
   grade.view(sim=wm) 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
    
main_account_screen()
