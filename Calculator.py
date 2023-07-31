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
bar2 = ''
numbers_list = []
oper_list = []
numbers2_list = []
operations = ['+', '-', '×', '÷']

Bar = Label(win, text=f'{bar}', font='bold')
Bar.pack(side='top')


# Calculate
def calc():
    global numbers, numbers2, result, Result
    if '+' in oper:
        if '.' not in numbers and numbers2:
            result = int(numbers) + int(numbers2)
        elif '.' in numbers or numbers2:
            result = float(numbers) + float(numbers2)

    elif '-' in oper:
        if '.' not in numbers and numbers2:
            result = int(numbers) - int(numbers2)
        elif '.' in numbers or numbers2:
            result = float(numbers) - float(numbers2)

    elif '×' in oper:
        if '.' not in numbers and numbers2:
            result = int(numbers) * int(numbers2)
        elif '.' in numbers or numbers2:
            result = float(numbers) * float(numbers2)

    elif '÷' in oper:
        if '.' not in numbers and numbers2:
            result = int(numbers) // int(numbers2)
        elif '.' in numbers or numbers2:
            result = float(numbers) / float(numbers2)

    Result.destroy()
    Result = Label(win, text=f'{result}', font='bold')
    Result.pack(side='top')
    Result.update()


# function numbers
def one_():
    global numbers, oper, numbers2, Bar, bar
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
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
    if oper not in operations:
        numbers = numbers + '9'
    else:
        numbers2 = numbers2 + '9'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def zero_():
    global numbers, numbers2, Bar, bar
    if oper not in operations:
        numbers = numbers + '0'
    else:
        numbers2 = numbers2 + '0'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def decimal_():
    global numbers, numbers2, Bar, bar
    if '+' or '-' not in oper:
        numbers = numbers + '.'
    else:
        numbers2 = numbers2 + '.'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


# Operator functions
def add_():
    global oper, Bar, bar
    oper = '+'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def subtract_():
    global oper, Bar, bar
    oper = '-'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def multiply_():
    global oper, Bar, bar
    oper = '×'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def divide_():
    global oper, Bar, bar
    oper = '÷'
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def backspace_():
    global Bar, bar, bar2, numbers2_list, numbers2, numbers_list, numbers, oper, oper_list
    numbers2_list = list(numbers2)
    numbers_list = list(numbers)
    oper_list = list(oper)

    if len(numbers2_list) > 0:
        del numbers2_list[len(numbers2_list) - 1]
        numbers2 = ''
        for i in numbers2_list:
            numbers2.join(i)
            bar = numbers + oper + numbers2

    elif len(oper_list) > 0:
        del oper_list[len(oper_list) - 1]
        oper = ''
        for i in oper_list:
            oper.join(i)
            bar = numbers + oper + numbers2

    elif len(numbers_list) > 0:
        del numbers_list[len(numbers_list) - 1]
        numbers = ''
        for i in numbers_list:
            numbers.join(i)
            bar = numbers + oper + numbers2

    bar2 = list(bar)
    del bar2[-1]
    bar = ''
    bar = bar.join(bar2)
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def ac_():
    global numbers, numbers2, oper, bar, Bar, result, Result
    numbers = ''
    numbers2 = ''
    oper = ''
    result = ''
    bar = numbers + oper + numbers2
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()
    Result.destroy()
    Result = Label(win, text=f'{result}', font='bold')
    Result.pack(side='top')
    Result.update()


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

zero = Button(win, text='0', font='bold', command=zero_, height=2, width=4)
zero.place(x=550, y=400)

dot = Button(win, text='.', font='bold', command=decimal_, height=2, width=4)
dot.place(x=600, y=400)

add = Button(win, text='+', font='bold', command=add_, height=2, width=4)
add.place(x=650, y=300)

subtract = Button(win, text='-', font='bold', command=subtract_, height=2, width=4)
subtract.place(x=650, y=250)

multiply = Button(win, text='×', font='bold', command=multiply_, height=2, width=4)
multiply.place(x=600, y=200)

divide = Button(win, text='÷', font='bold', command=divide_, height=2, width=4)
divide.place(x=550, y=200)

backspace = Button(win, text='Bksp', font='bold', command=backspace_, height=2, width=4)
backspace.place(x=650, y=200)

ac = Button(win, text='AC', font='bold', command=ac_, height=2, width=4)
ac.place(x=500, y=200)

equal = Button(win, text='=', font='bold', command=calc, height=5, width=4)
equal.place(x=650, y=350)


# Labels

Result = Label(win, text='', font='bold')
Result.pack(side='top')
Result.update()

win.mainloop()
