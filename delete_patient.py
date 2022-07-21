from tkinter import *
import os


def login_verify_pat():
    password1 = pat_name.get()

    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_pat(password1)
            return TRUE
    password_not_recognised()


def password_not_recognised():
    global deleted_success
    deleted_success = Toplevel(main_screen)
    deleted_success.title('Confirmation')
    deleted_success.configure(bg='#ffffff')
    deleted_success.geometry('350x150')
    Label(deleted_success, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times', width="512",
          height="2").pack()
    Label(deleted_success, text='Patient does not Exist', font='garamond', bg='#ffffff', fg='white').pack()
    Label(deleted_success, bg='#ffffff').pack()
    Button(deleted_success, text='Try Again', width=10, height=1, font='Times', fg='white', bg='#3d9fb3', borderwidth=5,
           command=main_pagee).pack()


def main_pagee():
    deleted_success.destroy()


def login_success_pat(pas):
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Hospital Management System')
    password_not_recog_screen.geometry('350x150')
    password_not_recog_screen.configure(bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times',
          width="512", height="2").pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Label(password_not_recog_screen, text='Patient deleted Successfully!', font='Garamond', fg='black',
          bg='#ffffff').pack()
    temp = list()
    fhand = open("patient.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("patient.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')


def main_page():
    global main_screen
    global pat_name
    global name_emp_entry
    main_screen = Tk()
    main_screen.configure(bg='#ffffff')
    main_screen.geometry("350x250")
    main_screen.title('Delete Patient')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times', width="512", height="2").pack()
    Label(text='', bg='#ffffff').pack()
    Label(main_screen, text="Enter the Mobile Number:", font='Times', fg='black', bg='#ffffff').pack()
    Label(text='', bg='#ffffff').pack()
    pat_name = StringVar()
    pat_name_entry = Entry(main_screen, textvariable=pat_name)
    pat_name_entry.pack()
    Label(text='', bg='#ffffff').pack()
    Button(text='Delete', width=20, height=1, font='Times', fg='white', bg='#3d9fb3', borderwidth=3,
           command=login_verify_pat).pack()
    Label(text='', bg='#ffffff').pack()

    main_screen.mainloop()


main_page()