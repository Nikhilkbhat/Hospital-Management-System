from tkinter import *
import os

def med_verify():
    dId = dname_med.get()
    dname = dId_med.get()
    dno = dno_med.get()
    dspcl = dspcl_med.get()
    address = address_med.get()

    dname_med_entry.delete(0, END)
    dId_med_entry.delete(0, END)
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
    password_not_recog_screen.title('Hospital Management System')
    password_not_recog_screen.geometry('350x100')
    password_not_recog_screen.configure( bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM",  bg='#ffffff', fg='black', font='verdana',width="512", height="2").pack()
    Label(text='', bg='#ffffff').pack()
    Label(password_not_recog_screen, text='ID Already Exist!', font='arial',fg='black', bg='#ffffff').pack()
    Label(text='', bg='#ffffff').pack()
    Button(password_not_recog_screen, text='Try Again',fg='black', bg='#ffffff',font='garamond', command=main_page,borderwidth='5px').pack()

def insert_med(dnamee,dId,dno,dspcl,address):
    global book_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Doctor Added')
    password_not_recog_screen.geometry('330x150')
    password_not_recog_screen.configure( bg='#ffffff')
    Label(password_not_recog_screen, text="HOSPITAL MANAGEMENT SYSTEM",  bg='#3d9fb3', fg='black', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, bg='#ffffff').pack()
    Label(password_not_recog_screen, text='Doctor Added Successfully!', font='Garamond',fg='black', bg='#ffffff').pack()
    file=open('doctor.txt', 'a')
    file.write(dnamee)
    file.write(" ")
    file.write(dId)
    file.write(" ")
    file.write(dno)
    file.write(" ")
    file.write(dspcl)
    file.write(" ")
    file.write(address)
    file.write(" ")
    file.write("\n")



def main_page():
    global main_screen
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
    main_screen.configure( bg='#ffffff')
    main_screen.geometry("330x400")
    main_screen.title('Add Doctor')
    Label(text="HOSPITAL MANAGEMENT SYSTEM", bg='#3d9fb3', fg='black', font='Times', width="512", height="2").pack()
    Label(main_screen,text="Enter the Doctor Details:",font='Times',fg='black', bg='#ffffff',height='2').pack()
    dname_med = StringVar()
    dId_med = StringVar()
    dno_med = StringVar()
    dspcl_med = StringVar()
    address_med=StringVar()

    Label(main_screen, text='Name:', font='garamond', fg='black', bg='#ffffff').pack()
    dname_med_entry = Entry(main_screen, textvariable=dname_med)
    dname_med_entry.pack()
    Label(main_screen, text='Id:', font='garamond', fg='black', bg='#ffffff').pack()
    dId_med_entry = Entry(main_screen, textvariable=dId_med)
    dId_med_entry.pack()
    Label(main_screen, text='Phone number', font='garamond', fg='black', bg='#ffffff').pack()
    dno_med_entry = Entry(main_screen, textvariable=dno_med)
    dno_med_entry.pack()
    Label(main_screen, text='Specialization:', font='garamond', fg='black', bg='#ffffff').pack()
    dspcl_med_entry = Entry(main_screen, textvariable=dspcl_med)
    dspcl_med_entry.pack()
    Label(main_screen, text='Address:', font='garamond', fg='black', bg='#ffffff').pack()
    address_med_entry = Entry(main_screen, textvariable=address_med)
    address_med_entry.pack()
    Label( bg='#ffffff').pack()
    Button(main_screen, text='Add Doctor', width=20, height=1, font='Times', fg='black', bg='#3d9fb3',borderwidth=5, command=med_verify).pack()
    main_screen.mainloop()
main_page()