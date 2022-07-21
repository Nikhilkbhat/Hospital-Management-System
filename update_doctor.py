from tkinter import *
import os

def med_verify():
    dname = pas
    dId = dId_med.get()
    dno = dno_med.get()
    dspcl = dspcl_med.get()
    address = address_med.get()

    dname_med_entry.delete(0, END)
    dId_med_entry.delete(0,END)
    dno_med_entry.delete(0, END)
    dspcl_med_entry.delete(0, END)
    address_med_entry.delete(0,END)

    for line in open("doctor.txt", "r").readlines():
        login_info = line.split()
        if dId == login_info:
            med_exist()
            return TRUE
    insert_med(dname,dId,dno,dspcl,address)

def med_exist():
    global med_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Update Doctor')
    password_not_recog_screen.geometry('360x150')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#ffffff', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='ID Already Exists',font='Times',bg='#ffffff', fg='white').pack()
    Label(password_not_recog_screen,bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#3d9fb3',borderwidth=5).pack()
    #, command=main_page

def insert_med(dname,dId,dnok,dspcl,address):
    global med_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Doctor Updated')
    password_not_recog_screen.geometry('350x100')
    password_not_recog_screen.configure( bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", fg='white', font='Times',width="512", bg='#3d9fb3', height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Doctor Updated Successfully', font='Garamond', bg='#ffffff',fg='black').pack()
    file=open('doctor.txt', 'a')
    file.write(dname)
    file.write(" ")
    file.write(dId)
    file.write(" ")
    file.write(dnok)
    file.write(" ")
    file.write(dspcl)
    file.write(" ")
    file.write(address)
    file.write(" ")
    file.write("\n")

def delete_existing(pas):
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



def login_verify_med():
    password1 = med_id.get()

    for line in open("doctor.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_med(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Invalid')
    password_not_recog_screen.configure(bg='#ffffff')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen,text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='Doctor does not Exist',font='Times',bg='#ffffff', fg='black').pack()
    Label(password_not_recog_screen,bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#3d9fb3',borderwidth=5,command=main_pagee).pack()
    
def main_pagee():
    password_not_recog_screen.destroy()    

def login_success_med(upas):
    global login_success_screen
    global dname_med
    global dname_med_entry
    global dId_med
    global dId_med_entry
    global dno_med
    global dno_med_entry
    global dspcl_med
    global dspcl_med_entry
    global address_med
    global address_med_entry
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Doctor Doctor')
    login_success_screen.geometry('350x400')
    login_success_screen.configure(bg="white")
    Label(login_success_screen,text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times',width="512", height="2").pack()
    Label(bg="white").pack()
    Label(login_success_screen, text='Doctor Details Are:',font='Times',fg='black', bg='#ffffff').pack()
    Label(bg="white").pack()
    for line in open("doctor.txt", "r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(bg="white").pack()
            Label(login_success_screen, text='ID',font='Times',fg='black', bg='#ffffff').pack()
            Label(bg="white").pack()
            Label(bg="white").pack()
            Label(login_success_screen, text=login_info[0],font='Times',fg='black', bg='#ffffff').pack()
            Label(login_success_screen, text='Name',font='Times',fg='black', bg='#ffffff').pack()
            Label(bg="white").pack()
            Label(text='').pack()
            dId_med_entry = Entry(login_success_screen, textvariable=dId_med)
            dId_med_entry.pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Phone No:',font='Times',fg='black', bg='#ffffff').pack()
            Label(text='').pack()
            Label(text='').pack()
            dno_med_entry = Entry(login_success_screen, textvariable=dno_med)
            dno_med_entry.pack()
            Label(login_success_screen, text='Specialization:',font='Times',fg='black', bg='#ffffff').pack()
            Label(text='').pack()
            Label(text='').pack()
            dspcl_med_entry = Entry(login_success_screen, textvariable=dspcl_med)
            dspcl_med_entry.pack()
            Label(login_success_screen, text='Address:',font='Times',fg='black', bg='#ffffff').pack()
            Label(text='').pack()
            Label(text='').pack()
            address_med_entry = Entry(login_success_screen, textvariable=address_med)
            address_med_entry.pack()
        else:
            continue
        Label(login_success_screen,bg='white').pack()
    Button(login_success_screen, text='Update Doctor', width=20, font='Times', fg='white', bg='#3d9fb3',borderwidth=5,command=med_verify).pack()

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global med_id
    global dname_med_entry
    global dname_med
    global dname_med_entry
    global dId_med
    global dId_med_entry
    global dno_med
    global dno_med_entry
    global dspcl_med
    global dspcl_med_entry
    global address_med
    global address_med_entry
    main_screen = Tk()
    main_screen.geometry("330x210")
    main_screen.configure(bg    ="#ffffff")
    main_screen.title('Update Doctor')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='white', font='Times',width="512", height="2").pack()
    Label(bg='#ffffff').pack()
    Label(main_screen,text="Enter the Doctor id:", font='Times',fg='black', bg='#ffffff').pack()
    Label(bg='#ffffff').pack()
    med_id=StringVar()
    dname_med_entry= Entry(main_screen, textvariable=med_id)
    dname_med_entry.pack()
    Label(bg='#ffffff').pack()
    Button(text='Update',width=20, font='Times', fg='white', bg='#3d9fb3',borderwidth=5,command=login_verify_med).pack()
    dname_med = StringVar()
    dId_med = StringVar()
    dno_med = StringVar()
    dspcl_med = StringVar()
    address_med=StringVar()
    main_screen.mainloop()


main_page()