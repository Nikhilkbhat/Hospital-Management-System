from tkinter import *
import os


def pat_verify():
    user = name_pat.get()
    id = pas
    address = address_pat.get()
    ph = ph_pat.get()

    name_pat_entry.delete(0, END)
    address_pat_entry.delete(0, END)
    ph_pat_entry.delete(0, END)

    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if id == login_info:
            pat_exist()
            return TRUE
    insert_pat(user, id, address, ph)


def insert_pat(userr, idd, addresss, phh):
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Patient Updated')
    password_not_recog_screen.geometry('330x120')
    password_not_recog_screen.configure(bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", fg='white', font='Times', width="512",
          bg='#3d9fb3', height="2").pack()
    Label(password_not_recog_screen, bg="white").pack()
    Label(password_not_recog_screen, text='Patient Updated Succesfully', font='Garamond', bg='#ffffff',
          fg='black').pack()
    file = open('patient.txt', 'a')
    file.write(idd)
    file.write(" ")
    file.write(userr)
    file.write(" ")
    file.write(addresss)
    file.write(" ")
    file.write(phh)
    file.write(" ")
    file.write("\n")


def pat_exist():
    global pat_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Update Patient')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#ffffff', fg='white', font='Times',
          width="512", height="2").pack()
    Label(password_not_recog_screen, text='ID Already Exists', font='Times', bg='#ffffff', fg='white').pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again', width=10, height=1, font='Times', fg='white', bg='#3d9fb3',
           borderwidth=5).pack()
    # , command=main_page


def delete_existing(pas):
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


def login_verify_pat():
    password1 = pat_id.get()

    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_pat(password1)
            return TRUE
    password_not_recognised()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Invalid')
    password_not_recog_screen.configure(bg='#ffffff')
    password_not_recog_screen.geometry('330x170')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times',
          width="512", height="2").pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Label(password_not_recog_screen, text='Patient does not Exist', font='Times', bg='#ffffff', fg='black').pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again', width=10, height=1, font='Times', fg='white', bg='#3d9fb3',
           borderwidth=5, command=main_pagee).pack()


def main_pagee():
    password_not_recog_screen.destroy()


def login_success_pat(upas):
    global login_success_screen
    global name_emp_entry
    global name_pat_entry
    global id_pat
    global id_pat_entry
    global address_pat
    global address_pat_entry
    global ph_pat
    global ph_pat_entry
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Update Doctor')
    login_success_screen.geometry('330x300')
    login_success_screen.configure(bg="white")
    Label(login_success_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times', width="512",
          height="2").pack()
    Label(bg="white").pack()
    Label(login_success_screen, text='Update patient With:', font='Times', fg='white', bg='#ffffff').pack()
    Label(bg="white").pack()
    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(login_success_screen, text='Phone Number', font='Times', fg='black', bg='#ffffff').pack()
            Label(bg="white").pack()
            Label(bg="white").pack()
            Label(login_success_screen, text=login_info[0], font='Times', fg='black', bg='#ffffff').pack()
            Label(login_success_screen, text='Name:', font='Times', fg='black', bg='#ffffff').pack()
            Label(bg="white").pack()
            Label(bg="white").pack()
            address_pat_entry = Entry(login_success_screen, textvariable=name_pat)
            address_pat_entry.pack()
            Label(login_success_screen, text='Address', font='Times', fg='black', bg='#ffffff').pack()
            Label(bg="white").pack()
            Label(bg="white").pack()
            ph_pat_entry = Entry(login_success_screen, textvariable=address_pat)
            ph_pat_entry.pack()
        else:
            continue
        Label(login_success_screen, bg='#ffffff').pack()
    Button(login_success_screen, text='Update Patient', width=20, font='Times', fg='white', bg='#3d9fb3', borderwidth=5,
           command=pat_verify).pack()


def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global pat_id
    global name_emp_entry
    global name_pat
    global name_pat_entry
    global id_pat
    global id_pat_entry
    global address_pat
    global address_pat_entry
    global ph_pat
    global ph_pat_entry
    main_screen = Tk()
    main_screen.geometry("330x210")
    main_screen.configure(bg="#ffffff")
    main_screen.title('Update patient')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times', width="512", height="2").pack()
    Label(bg='#ffffff').pack()
    Label(main_screen, text="Enter the Mobile Number:", font='Times', fg='black', bg='#ffffff').pack()
    Label(bg='#ffffff').pack()
    pat_id = StringVar()
    name_pat_entry = Entry(main_screen, textvariable=pat_id)
    name_pat_entry.pack()
    Label(bg='#ffffff').pack()
    Button(text='Update', width=20, font='Times', fg='white', bg='#3d9fb3', borderwidth=5,
           command=login_verify_pat).pack()
    name_pat = StringVar()
    id_pat = StringVar()
    address_pat = StringVar()
    ph_pat = StringVar()

    main_screen.mainloop()


main_page()