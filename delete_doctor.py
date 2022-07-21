from tkinter import *
import os

def login_verify_med():
    password1 = med_mname.get()

    for line in open("doctor.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_book(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.configure(bg='#000000')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen,text="HOSPITAL MANAGEMENT SYSTEM",bg='#3d9fb3', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='Doctor does not Exist',font='garamond',bg='#000000',fg='white').pack()
    Label(password_not_recog_screen, bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#3d9fb3',borderwidth=5, command=main_pagee).pack()
    
def main_pagee():
    password_not_recog_screen.destroy()    

def login_success_book(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Doctor Deleted')
    login_success_screen.geometry('350x125')
    login_success_screen.configure(bg='#000000')
    Label(login_success_screen,text="HOSPITAL MANAGEMENT SYSTEM",  bg='#3d9fb3', fg='white', font='Times',width="512", height="2").pack()
    Label(login_success_screen,bg='#000000').pack()
    Label(login_success_screen, text='Doctor Deleted Successfully', font='Garamond',fg='white',bg='#000000').pack()
    
    temp = list()
    fhand = open("doctor.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("doctor.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global med_mname
    global mname_med_entry
    main_screen = Tk()
    main_screen.configure(bg='#000000')
    main_screen.geometry("330x220")
    main_screen.title('Delete Doctor')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times', width="512", height="2").pack()
    Label(bg='#000000').pack()
    Label(main_screen,text="Enter the Doctor ID:",font='Times',fg='white',bg='#000000').pack()
    Label(bg='#000000').pack()
    med_mname=StringVar()
    mname_med_entry= Entry(main_screen, textvariable=med_mname)
    mname_med_entry.pack()
    Label(bg='#000000').pack()
    Button(text='Enter',width=20, height=1, font='Times', fg='white', bg='#3d9fb3',borderwidth=3,command=login_verify_med).pack()
    main_screen.mainloop()


main_page()