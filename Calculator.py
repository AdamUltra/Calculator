from tkinter import *
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.title(" Calculator by AdamUltra ")
numbers = ''
numbers2 = ''
oper = ''
bar = ''

Bar = Label(win, text=f'{bar}', font='bold')
Bar.pack(side='top')


# Calculate
def calc():
    global result, numbers, numbers2
    result = int(numbers) + int(numbers2)
    Result = Label(win, text=f'{result}', font='bold')
    Result.pack(side='top')
    Result.update()


# function numbers
def one_():
    global numbers, oper, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '1'
    else:
        numbers2 = numbers2 + '1'

    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def two_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '2'
    else:
        numbers2 = numbers2 + '2'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def three_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '3'
    else:
        numbers2 = numbers2 + '3'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def four_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '4'
    else:
        numbers2 = numbers2 + '4'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def five_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '5'
    else:
        numbers2 = numbers2 + '5'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def six_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '6'
    else:
        numbers2 = numbers2 + '6'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def seven_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '7'
    else:
        numbers2 = numbers2 + '7'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def eight_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '8'
    else:
        numbers2 = numbers2 + '8'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def nine_():
    global numbers, numbers2, Bar, bar
    if '+' not in oper:
        numbers = numbers + '9'
    else:
        numbers2 = numbers2 + '9'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()

def add_():
    global oper, Bar, bar
    oper = '+'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


# Numbers

one = Button(win, text='1', font='bold', command=one_, height=2, width=4)
one.place(x=500, y=250)

two = Button(win, text='2', font='bold', command=two_, height=2, width=4)
two.place(x=550, y=250)

three = Button(win, text='3', font='bold', command=three_, height=2, width=4)
three.place(x=600, y=250)

four = Button(win, text='4', font='bold', command=four_, height=2, width=4)
four.place(x=500, y=300)

five = Button(win, text='5', font='bold', command=five_, height=2, width=4)
five.place(x=550, y=300)

six = Button(win, text='6', font='bold', command=six_, height=2, width=4)
six.place(x=600, y=300)

seven = Button(win, text='7', font='bold', command=seven_, height=2, width=4)
seven.place(x=500, y=350)

eight = Button(win, text='8', font='bold', command=eight_, height=2, width=4)
eight.place(x=550, y=350)

nine = Button(win, text='9', font='bold', command=nine_, height=2, width=4)
nine.place(x=600, y=350)

add = Button(win, text='+', font='bold', command=add_, height=2, width=4)
add.place(x=650, y=300)

equal = Button(win, text='=', font='bold', command=calc, height=5, width=4)
equal.place(x=650, y=350)

win.mainloop()
