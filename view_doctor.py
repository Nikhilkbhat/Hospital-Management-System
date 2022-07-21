from tkinter import *
import os


def main_page():
    global main_screen
    main_screen1 = Tk()
    main_screen1.title('View Doctor')
    main_screen1.configure(bg="#ffffff")
    main_screen1.geometry('750x300')
    frame = Frame(main_screen1)
    grid = Frame(frame)
    Label(main_screen1, text='                         ', bg='#ffffff').grid(row=0)
    Label(main_screen1, text="Doctor Details", font='Times', bg='#ffffff', fg='black', width=18).grid(row=1, column=1,
                                                                                                        columnspan=7)
    Label(main_screen1, text='  ', bg='#ffffff').grid(row=2)
    Label(main_screen1, text='      ID ', font='Garamond', fg='white', bg='#3d9fb3').grid(row=3, column=1)
    Label(main_screen1, text='                 ', bg='#ffffff').grid(row=3)
    Label(main_screen1, text='       Name   ', font='Garamond', fg='white', bg='#3d9fb3').grid(row=3, column=3)
    Label(main_screen1, text='               ', bg='#ffffff').grid(row=3)
    Label(main_screen1, text='     Phone No      ', font='Garamond', fg='white', bg='#3d9fb3').grid(row=3, column=5)
    Label(main_screen1, text='                   ', bg='#ffffff').grid(row=3)
    Label(main_screen1, text='      Specialization    ', font='Garamond', fg='white', bg='#3d9fb3').grid(row=3, column=7)
    Label(main_screen1, text='                   ', bg='#ffffff').grid(row=3)
    Label(main_screen1, text='      Address     ', font='Garamond', fg='white', bg='#3d9fb3').grid(row=3, column=9)
    i = 10
    for line in open("doctor.txt", "r").readlines():
        cus = line.split()
        Label(main_screen1, text=cus[0], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=1)
        Label(main_screen1, text=cus[1], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=3)
        Label(main_screen1, text=cus[2], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=5)
        Label(main_screen1, text=cus[3], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=7)
        Label(main_screen1, text=cus[4], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=9)
        i = i + 1

    main_screen1.mainloop()


main_page() 