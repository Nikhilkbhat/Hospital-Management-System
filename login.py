from tkinter import *
from tkinter import messagebox
import os

def add_doctor():
    os.system('python add_doctor.py')

def view_doctor():
    os.system('python view_doctor.py')

def search_doctor():
    os.system('python search_doctor.py')

def update_doctor():
    os.system('python update_doctor.py')

def delete_doctor():
    os.system('python delete_doctor.py')



def add_patient():
    os.system('python add_patient.py')

def view_patient():
    os.system('python view_patient.py')

def search_patient():
    os.system('python search_patient.py')

def update_patient():
    os.system('python update_patient.py')

def delete_patient():
    os.system('python delete_patient.py')




def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = Toplevel(main_screen)
    login_screen.title('Admin Login')
    login_screen.geometry('275x275')
    login_screen.configure(bg="#FFFFFF")
    Label(login_screen,bg="#FFFFFF").pack()
    Label(login_screen, text='Enter Admin Credentials', fg='black',bg='#3d9fb3', font='Times',height=2,width=512).pack()
    Label(login_screen, bg="#FFFFFF").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username',font='Garamond',bg="#FFFFFF",fg="black").pack()
    Label(bg="#FFFFFF").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='',bg="#FFFFFF").pack()
    Label(login_screen, text='Password',font='Garamond',bg="#FFFFFF",fg="black").pack()
    Label(bg="#FFFFFF").pack()
    Label(bg="#FFFFFF").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text='',bg="#FFFFFF").pack()
    Button(login_screen, text='LOGIN', width=10, height=0,font='Garamond',borderwidth=5,bg='#3d9fb3',fg='black' ,command=login_verify).pack()




def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    for line in open("login.txt", "r").readlines():
        login_info = line.split()
        if username1 == login_info[0] and password1 == login_info[1]:
            login_success()
            return TRUE
    password_not_recognised()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Login Success')
    login_success_screen.geometry('200x200')
    login_success_screen.configure(bg="#FFFFFF")
    Label(login_success_screen,bg="#FFFFFF").pack()
    Label(login_success_screen, text='Login Success',bg="#3d9fb3",height=1,fg='black',font="Times",width=512).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Label(command=admin_button()).pack()



def admin_button():
    login_success_screen.geometry('400x750')
    Button(login_success_screen, text='Add Doctor', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=add_doctor).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='View Doctor', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=view_doctor).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Search Doctors', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=search_doctor).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Delete Doctor', font='Times', height=1, width=30, fg='black',bg='#3d9fb3',command=delete_doctor).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Update Doctor Details', font='Times', height=1, width=30, fg='black',bg='#3d9fb3',command=update_doctor).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()



    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Add New Patient', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=add_patient).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='View Patients', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=view_patient).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Search Patient', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=search_patient).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Delete Patient', font='Times', height=1, width=30, fg='black', bg='#3d9fb3',command=delete_patient).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()
    Button(login_success_screen, text='Update Patient Details',font='Times', height=1, width=30, fg='black',bg='#3d9fb3',command=update_patient).pack()
    Label(login_success_screen,bg="#FFFFFF").pack()

    Button(login_success_screen,text='LOGOUT', height='1', width='20',font='garamond',borderwidth=5,bg='#3d9fb3',fg="black",command=view_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.geometry('250x250')
    password_not_recog_screen.configure(bg="#FFFFFF")
    Label(password_not_recog_screen,bg="#FFFFFF").pack()
    Label(password_not_recog_screen, text='Invalid Credentials',font="Times",bg="#FFFFFF",width=20,fg="black").pack()
    Label(password_not_recog_screen,bg="#FFFFFF").pack()
    Label(password_not_recog_screen,bg="#FFFFFF").pack()
    Button(password_not_recog_screen, text='OK',height='1', width='15',font='garamond', borderwidth=5,bg='#3d9fb3',fg='black', command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('User not found')
    user_not_found_screen.geometry('212x212')
    Label(user_not_found_screen, text='User not found').pack()
    Button(user_not_found_screen, text='OK', command=delete_user_not_found).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found():
    user_not_found_screen.destroy()

def view_success():
    main_screen.destroy()

def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="#FFFFFF")
    main_screen.geometry("330x200")
    main_screen.title('Home')
    Label(text="HOSPITAL MANAGEMENT SYSTEM",bg='#3d9fb3', fg='black', font='Times',width="512", height="2").pack()
    Label(bg='#FFFFFF').pack()
    Label(text='Login Here', height='1',font='Times',bg='#FFFFFF',fg="black").pack()
    Label(bg='#FFFFFF').pack()
    Button(text='ADMIN', height='1', width='20',font='garamond', command=login,borderwidth=5,bg='#3d9fb3',fg="black").pack()

    main_screen.mainloop()


main_page()

