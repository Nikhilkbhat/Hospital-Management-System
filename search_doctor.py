from tkinter import *
import os

def login_verify_med():
    password1 = med_mname.get()

    for line in open("doctor.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_med(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.configure(bg='#ffffff')
    password_not_recog_screen.geometry('330x150')
    Label(password_not_recog_screen,text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='black', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='Doctor is not Available',font='Times',bg='#ffffff', fg='black').pack()
    Label(password_not_recog_screen,bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='black', bg='#3d9fb3',borderwidth=5, command=main_pagee).pack()
   
def main_pagee():
    password_not_recog_screen.destroy()   

def login_success_med(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Doctor')
    login_success_screen.geometry('700x200')
    login_success_screen.configure(bg="white")
    frame = Frame(login_success_screen)
    grid=Frame(frame)
    Label(login_success_screen, text='                         ',bg='#ffffff').grid(row=0)
    Label(login_success_screen, text="Doctor Details",font='Times',bg='white',fg='black',width=18).grid(row=1, column=1, columnspan=7)
    Label(login_success_screen, text='  ',bg='#ffffff').grid(row=2)
    Label(login_success_screen, text='    ID   ',font='Garamond',fg='black',bg='#3d9fb3').grid(row=3, column=1)
    Label(login_success_screen, text='                 ',bg='#ffffff').grid(row=3)
    Label(login_success_screen, text='   Name       ',font='Garamond',fg='black',bg='#3d9fb3').grid(row=3, column=3)
    Label(login_success_screen, text='               ',bg='#ffffff').grid(row=3)
    Label(login_success_screen, text='     Phone No      ',font='Garamond',fg='black',bg='#3d9fb3').grid(row=3, column=5)
    Label(login_success_screen, text='                   ',bg='#ffffff').grid(row=3)
    Label(login_success_screen, text='      Specialization    ',font='Garamond',fg='black',bg='#3d9fb3').grid(row=3, column=7)
    Label(login_success_screen, text="              ",bg="white").grid(row=3)
    Label(login_success_screen, text='      Address    ',font='Garamond',fg='black',bg='#3d9fb3').grid(row=3, column=9)
    Label(login_success_screen, text="              ",bg="white").grid(row=6)
    
    i=5
    for line in open("doctor.txt", "r").readlines():
        cus = line.split()
        if pas == cus[0]:
            Label(login_success_screen, text=cus[0],font='Garamond',fg='black',bg='#ffffff').grid(row=i, column=1)
            Label(login_success_screen, text=cus[1],font='Garamond',fg='black',bg='#ffffff').grid(row=i, column=3)
            Label(login_success_screen, text=cus[2],font='Garamond',fg='black',bg='#ffffff').grid(row=i, column=5)
            Label(login_success_screen, text=cus[3],font='Garamond',fg='black',bg='#ffffff').grid(row=i, column=7)
            Label(login_success_screen, text=cus[4],font='Garamond',fg='black',bg='#ffffff').grid(row=i, column=9)
        else:
            continue
    Button(login_success_screen, text='OK', width=5, height=1,font='Garamond',borderwidth=2,bg='#3d9fb3',fg="black", command=delete_login_success).grid(row=i+2,column=1,columnspan=7)

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global med_mname
    global med_mname_entry
    main_screen = Tk() 
    main_screen.configure(bg="#ffffff")
    main_screen.geometry("330x220")
    main_screen.title('Search Doctor')
    Label(text="HOSPITAL MANAGEMENT SYSTEM",bg='#3d9fb3', fg='black', font='Times',width="512", height="2").pack()
    Label(text='',bg='#ffffff').pack()
    Label(main_screen,text="Enter Doctor ID:",font='Times',bg='#ffffff',fg="black").pack()
    Label(text='',bg='#ffffff').pack()
    med_mname=StringVar()
    med_mname_entry= Entry(main_screen, textvariable=med_mname)
    med_mname_entry.pack()
    Label(text='',bg='#ffffff').pack()
    Button(text='Search', width='15',height=1,font='garamond',borderwidth=5,bg='#3d9fb3',fg="black",command=login_verify_med).pack()
    Label(text='',bg='#ffffff').pack()
    main_screen.mainloop()

main_page()