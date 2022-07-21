from tkinter import *
import os


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="#ffffff")
    main_screen.title('View Patient')
    main_screen.geometry('500x300')
    frame = Frame(main_screen)
    grid = Frame(frame)
    Label(main_screen, text='                         ', bg='#ffffff').grid(row=0)
    Label(main_screen, text="Patient Details", font='Times', bg='#ffffff', fg='black', width=18).grid(row=1, column=1,
                                                                                                      columnspan=7)
    Label(main_screen, text='               ', bg='#ffffff').grid(row=2)
    Label(main_screen, text='       Name      ', font='Garamond', bg='#3d9fb3', fg='white').grid(row=3, column=1)
    Label(main_screen, text='               ', bg='#ffffff').grid(row=3)
    Label(main_screen, text='   Address ', font='Garamond', bg='#3d9fb3', fg='white').grid(row=3, column=3)
    Label(main_screen, text='               ', bg='#ffffff').grid(row=4)
    Label(main_screen, text='     Phone Number   ', font='Garamond', bg='#3d9fb3', fg='white').grid(row=3, column=5)
    Label(main_screen, text='                   ', bg='#ffffff').grid(row=3)

    i = 8
    for line in open("patient.txt", "r").readlines():
        pat = line.split()
        Label(main_screen, text=pat[1], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=1)
        Label(main_screen, text=pat[2], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=3)
        Label(main_screen, text=pat[0], font='Garamond', fg='black', bg='#ffffff').grid(row=i, column=5)

        i = i + 1

    main_screen.mainloop()


main_page()    