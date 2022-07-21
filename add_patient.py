from tkinter import *
import os


def pat_verify():
    phone = phone_pat.get()
    user = name_pat.get()
    id = id_pat.get()
    address = address_pat.get()

    phone_pat_entry.delete(0, END)
    name_pat_entry.delete(0, END)
    # id_pat_entry.delete(0, END)
    address_pat_entry.delete(0, END)

    for line in open("patient.txt", "r").readlines():
        login_info = line.split()
        if id == login_info:
            user_exist()
            return TRUE
    insert_pat(phone, user, id, address)


rec = len(open("patient.txt", "r").readlines()) + 1


def autoincrement():
    global rec
    rec += 1
    id_pat_entry.configure(text=rec)


def user_exist():
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Hospital Management System')
    password_not_recog_screen.geometry('350x350')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='black', font='Times',
          width="512", height="2").pack()
    Label(text='', bg='#ffffff').pack()
    Label(password_not_recog_screen, text='ID Already Exist!', font='arial', fg='red').pack()
    Label(text='', bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again', fg='black', font='garamond', command=main_page,
           borderwidth='5px').pack()


def insert_pat(phonee, userr, idd, address):
    global userr_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Hospital Management System')
    password_not_recog_screen.geometry('350x120')
    password_not_recog_screen.configure(bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM", fg='black', font='Times', width="512",
          bg='#3d9fb3', height="2").pack()
    Label(password_not_recog_screen, bg='white').pack()
    Label(password_not_recog_screen, text='Patient Added Successfully', font='Garamond', bg='#ffffff', fg='black').pack()
    file = open('patient.txt', 'a')
    file.write(phonee)
    file.write(" ")
    file.write(userr)
    file.write(" ")
    file.write(idd)
    file.write(" ")
    file.write(address)
    file.write(" ")

    file.write("\n")
    autoincrement()
    # Button(password_not_recog_screen, text='OK', width=5, font='Times', fg='black', bg='#3d9fb3',borderwidth=5,command=main_page).pack()


def main_page():
    global main_screen
    global name_pat
    global name_pat_entry
    global id_pat
    global id_pat_entry
    global address_pat
    global address_pat_entry
    global phone_pat
    global phone_pat_entry
    main_screen = Tk()
    main_screen.configure(bg='#ffffff')
    main_screen.geometry("350x350")
    main_screen.title('Add Patient')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='black', font='Times', width="512", height="2").pack()
    Label(main_screen, text="Enter Patient Details:", font='Times', fg='black', bg='#ffffff').pack()
    phone_pat = StringVar()
    name_pat = StringVar()
    id_pat = StringVar()
    address_pat = StringVar()

    Label(main_screen, text='Phone No:', font='garamond', fg='black', bg='#ffffff').pack()
    phone_pat_entry = Entry(main_screen, textvariable=phone_pat)
    phone_pat_entry.pack()

    Label(main_screen, text='Name:', font='garamond', fg='black', bg='#ffffff').pack()
    name_pat_entry = Entry(main_screen, textvariable=name_pat)
    name_pat_entry.pack()

    Label(main_screen, text='Patient ID:', font='garamond', fg='black', bg='#ffffff').pack()
    id_pat_entry = Label(main_screen, text=rec, font='garamond', fg='black', bg='#ffffff')
    id_pat_entry.pack()

    Label(main_screen, text='Address:', font='garamond', fg='black', bg='#ffffff').pack()
    address_pat_entry = Entry(main_screen, textvariable=address_pat)
    address_pat_entry.pack()

    Label(main_screen, text='', bg='#ffffff').pack()

    Button(main_screen, text='Add Patient', width=20, font='Times', fg='black', bg='#3d9fb3', borderwidth=5,
           command=pat_verify).pack()
    main_screen.mainloop()


main_page()