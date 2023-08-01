from tkinter import *
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.title(" Calculator by AdamUltra ")
numbers = ''
i = ''
numbers2 = ''
numbers3 = ''
oper = ''
oper2 = ''
bar = ''
bar2 = ''
numbers_list = []
numbers2_list = []
numbers3_list = []
oper_list = []
oper2_list = []
operations = ['+', '-', '×', '÷']

Bar = Label(win, text=f'{bar}', font='bold')
Bar.pack(side='top')


# Calculate
def calc():
    global numbers, numbers2, result, Result
    if len(oper2) == 0:
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

    elif len(oper2) == 1:
        if '+' in oper and '-' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) + int(numbers2) - int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) + float(numbers2) - float(numbers3)

        elif '+' in oper and '+' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) + int(numbers2) + int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) + float(numbers2) + float(numbers3)

        elif '+' in oper and '×' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) + int(numbers2) * int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) + float(numbers2) * float(numbers3)

        elif '+' in oper and '÷' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) + int(numbers2) // int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) + float(numbers2) / float(numbers3)

        elif '-' in oper and '+' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) - int(numbers2) + int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) - float(numbers2) + float(numbers3)

        elif '-' in oper and '-' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) - int(numbers2) - int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) - float(numbers2) - float(numbers3)

        elif '-' in oper and '×' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) - int(numbers2) * int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) - float(numbers2) * float(numbers3)

        elif '-' in oper and '÷' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) - int(numbers2) // int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) - float(numbers2) / float(numbers3)

        elif '×' in oper and '+' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) * int(numbers2) + int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) * float(numbers2) + float(numbers3)

        elif '×' in oper and '-' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) * int(numbers2) - int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) * float(numbers2) - float(numbers3)

        elif '×' in oper and '×' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) * int(numbers2) * int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) * float(numbers2) * float(numbers3)

        elif '×' in oper and '÷' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) * int(numbers2) // int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) * float(numbers2) / float(numbers3)

        elif '÷' in oper and '×' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) // int(numbers2) * int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) / float(numbers2) * float(numbers3)

        elif '÷' in oper and '+' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) // int(numbers2) + int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) / float(numbers2) + float(numbers3)

        elif '÷' in oper and '-' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) // int(numbers2) - int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) / float(numbers2) - float(numbers3)

        elif '÷' in oper and '÷' in oper2:
            if '.' not in numbers and numbers2:
                result = int(numbers) // int(numbers2) // int(numbers3)
            elif '.' in numbers or numbers2:
                result = float(numbers) / float(numbers2) / float(numbers3)

    Result.destroy()
    Result = Label(win, text=f'{result}', font='bold')
    Result.pack(side='top')
    Result.update()


# function numbers
def one_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '1'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '1'
    elif oper2 in operations:
        numbers3 = numbers3 + '1'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def two_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '2'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '2'
    elif oper2 in operations:
        numbers3 = numbers3 + '2'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def three_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '3'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '3'
    elif oper2 in operations:
        numbers3 = numbers3 + '3'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def four_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '4'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '4'
    elif oper2 in operations:
        numbers3 = numbers3 + '4'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def five_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '5'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '5'
    elif oper2 in operations:
        numbers3 = numbers3 + '5'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def six_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '6'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '6'
    elif oper2 in operations:
        numbers3 = numbers3 + '6'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def seven_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '7'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '7'
    elif oper2 in operations:
        numbers3 = numbers3 + '7'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def eight_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '8'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '8'
    elif oper2 in operations:
        numbers3 = numbers3 + '8'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def nine_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '9'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '9'
    elif oper2 in operations:
        numbers3 = numbers3 + '9'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def zero_():
    global numbers, oper, numbers2, Bar, bar, numbers3, oper2
    if oper not in operations:
        numbers = numbers + '0'
    elif oper in operations and oper2 not in operations:
        numbers2 = numbers2 + '0'
    elif oper2 in operations:
        numbers3 = numbers3 + '0'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def decimal_():
    global numbers, numbers2, Bar, bar, numbers3
    if len(oper) == 0:
        numbers = numbers + '.'
    elif len(oper) == 1 and len(oper2) == 0:
        numbers2 = numbers2 + '.'
    elif len(oper2) == 1:
        numbers3 = numbers3 + '.'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


# Operator functions
def add_():
    global oper, Bar, bar, oper2
    if len(oper) == 0:
        oper = '+'

    elif len(oper) == 1:
        oper2 = '+'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def subtract_():
    global oper, Bar, bar, oper2
    if len(oper) == 0:
        oper = '-'

    elif len(oper) == 1:
        oper2 = '-'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def multiply_():
    global oper, Bar, bar, oper2
    if len(oper) == 0:
        oper = '×'

    elif len(oper) == 1:
        oper2 = '×'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


def divide_():
    global oper, Bar, bar, oper2
    if len(oper) == 0:
        oper = '÷'

    elif len(oper) == 1:
        oper2 = '÷'
    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


# delete only one number
def backspace_():
    global Bar, bar, bar2, numbers2_list, numbers2, numbers_list, numbers, oper, oper_list, oper2, oper2_list, numbers3, numbers3_list, i
    numbers3_list = list(numbers3)
    numbers2_list = list(numbers2)
    numbers_list = list(numbers)
    oper_list = list(oper)
    oper2_list = list(oper2)

    if len(numbers3) > 0:
        i = numbers3_list[-1]
        numbers3 = numbers3.replace(i, '')

    elif len(oper2) > 0:
        i = oper2_list[-1]
        oper2 = oper2.replace(i, '')

    elif len(numbers2) > 0:
        i = numbers2_list[-1]
        numbers2 = numbers2.replace(i, '')

    elif len(oper) > 0:
        i = oper_list[-1]
        oper = oper.replace(i, '')

    elif len(numbers) > 0:
        i = numbers_list[-1]
        numbers = numbers.replace(i, '')

    bar = numbers + oper + numbers2 + oper2 + numbers3
    Bar.destroy()
    Bar = Label(win, text=f'{bar}', font='bold')
    Bar.pack(side='top')
    Bar.update()


# delete all numbers
def ac_():
    global numbers, numbers2, oper, bar, Bar, result, Result, oper2, numbers3
    numbers = ''
    numbers2 = ''
    numbers3 = ''
    oper = ''
    oper2 = ''
    result = ''
    bar = numbers + oper + numbers2 + oper2 + numbers3
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
