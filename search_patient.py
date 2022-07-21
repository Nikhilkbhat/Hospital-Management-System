from tkinter import *
import os


def login_verify_pat():
    password1 = phone_pat.get()

    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_pat(password1)
            return TRUE
    password_not_recognised()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.configure(bg='#ffffff')
    password_not_recog_screen.geometry('360x200')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='black', font='Times',
          width="512", height="2").pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Label(password_not_recog_screen, text='Patient does not Exist', font='Times', bg='#ffffff', fg='black').pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again', width=10, height=1, font='Times', fg='black', bg='#3d9fb3',
           borderwidth=5, command=main_pagee).pack()


def main_pagee():
    password_not_recog_screen.destroy()


def login_success_pat(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.configure(bg="#ffffff")
    login_success_screen.geometry('550x250')
    frame = Frame(login_success_screen)
    grid = Frame(frame)
    Label(login_success_screen, text='                         ', bg='#ffffff').grid(row=0)
    Label(login_success_screen, text="Patient Details", font='Times', bg='white', fg='black', width=18).grid(row=1,
                                                                                                            column=1,
                                                                                                            columnspan=7)
    Label(login_success_screen, text='  ', bg='#ffffff').grid(row=2)
    Label(login_success_screen, text='    Name   ', font='Garamond', fg='black', bg='#3d9fb3').grid(row=3, column=1)
    Label(login_success_screen, text='                 ', bg='#ffffff').grid(row=3)
    Label(login_success_screen, text='     Address      ', font='Garamond', fg='black', bg='#3d9fb3').grid(row=3,
                                                                                                           column=3)
    Label(login_success_screen, text='                   ', bg='#ffffff').grid(row=3)
    Label(login_success_screen, text='    Phone Number    ', font='Garamond', fg='black', bg='#3d9fb3').grid(row=3,
                                                                                                             column=5)
    Label(login_success_screen, text="              ", bg="white").grid(row=5)

    i = 4
    for line in open("patient.txt", "r").readlines():
        pat = line.split()
        if pas == pat[0]:
            Label(login_success_screen, text=pat[1], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=1)
            Label(login_success_screen, text=pat[2], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=3)
            Label(login_success_screen, text=pat[0], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=5)
        else:
            continue
    Button(login_success_screen, text='OK', width=4, height=1, font='Garamond', borderwidth=3, bg='#3d9fb3', fg="black",
           command=delete_login_success).grid(row=i + 2, column=1, columnspan=7)


def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global phone_pat
    global name_emp_entry
    main_screen = Tk()
    main_screen.configure(bg="#ffffff")
    main_screen.geometry("330x230")
    main_screen.title('Search Patient')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg="#3d9fb3", fg="black", font='Times', width="512", height="2").pack()
    Label(bg='#ffffff').pack()
    Label(main_screen, text="Enter Mobile Number:", font='Times', bg="#ffffff", fg="black").pack()
    Label(bg='#ffffff').pack()
    phone_pat = StringVar()
    phone_pat_entry = Entry(main_screen, textvariable=phone_pat)
    phone_pat_entry.pack()
    Label(bg='#ffffff').pack()
    Button(text='Search', width='15', font='garamond', borderwidth=5, bg="#3d9fb3", fg="black",
           command=login_verify_pat).pack()
    Label(bg='#ffffff').pack()

    main_screen.mainloop()


main_page()
