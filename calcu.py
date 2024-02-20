import tkinter
from tkinter import *

window = Tk()
window.geometry('600x600')
window.title(' aratii Calculator ')
window.config(bg='pink')

equation = ''

def clear():
    global equation
    equation = ''
    l1.config(text=equation)

def show(value):
    global equation
    equation += value
    l1.config(text=equation)

def calculate():
    global equation
    result = ''
    if equation != '':
        try:
            result=eval(equation)
        except:
            result = 'error'
            equation = ''
    l1.config(text=result)


l1 = Label(window, width=20, height=3, text='', font=('Helvetica', 30), bg='#E6E6FA')
l1.pack()

b1 = Button(window, width=5, height=1, text='C', font=('ariel', 30, 'bold'), fg='#8e44ad', bg='#ecf0f1', command=lambda:clear())
b1.place(x=10, y=100)
b2 = Button(window, width=5, height=1, text='/', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('/'))
b2.place(x=150, y=100)
b3 = Button(window, width=5, height=1, text='%', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('%'))
b3.place(x=290, y=100)
b4 = Button(window, width=5, height=1, text='*', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('*'))
b4.place(x=430, y=100)
b5 = Button(window, width=5, height=1, text='7', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('7'))
b5.place(x=10, y=190)
b6 = Button(window, width=5, height=1, text='8', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('8'))
b6.place(x=150, y=190)
b7 = Button(window, width=5, height=1, text='9', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('9'))
b7.place(x=290, y=190)
b8 = Button(window, width=5, height=1, text='-', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('-'))
b8.place(x=430, y=190)
b9 = Button(window, width=5, height=1, text='4', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('4'))
b9.place(x=10, y=280)
b10 = Button(window, width=5, height=1, text='5', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('5'))
b10.place(x=150, y=280)
b11 = Button(window, width=5, height=1, text='6', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('6'))
b11.place(x=290, y=280)
b12 = Button(window, width=5, height=1, text='+', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('+'))
b12.place(x=430, y=280)
b13 = Button(window, width=5, height=1, text='1', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('1'))
b13.place(x=10, y=370)
b14 = Button(window, width=5, height=1, text='2', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('2'))
b14.place(x=150, y=370)
b15 = Button(window, width=5, height=1, text='3', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('3'))
b15.place(x=290, y=370)
b16 = Button(window, width=11, height=1, text='0', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('0'))
b16.place(x=10, y=460)
b17 = Button(window, width=5, height=1, text='.', font=('ariel', 30, 'bold'), fg='#fff', bg='#42484b', command=lambda:show('.'))
b17.place(x=290, y=460)
b18 = Button(window, width=5, height=3, text='=', font=('ariel', 30, 'bold'), fg='#8e44ad', bg='#ecf0f1', command=lambda:calculate())
b18.place(x=430, y=370)
window.mainloop()