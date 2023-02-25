import tkinter
window = tkinter.Tk()
window.title("My calculator")
window.geometry("300x500")


def get_num1():
    n = int(text_num1.get())
    return n


def set_answer(result):
    text_answer.delete(0, "end")
    text_answer.insert(0, result)


def get_num2():
    n = int(text_num2.get())
    return n


def add():  
    num1 = get_num1()
    num2 = get_num2()
    result = int(num1 + num2)
    set_answer(result)


def sub():
    num1 = get_num1()
    num2 = get_num2()
    result = int(num1 - num2)
    set_answer(result)


def mul():
    num1 = get_num1()
    num2 = get_num2()
    result = (num1 * num2)
    set_answer(result)


def div():
    num1 = get_num1()
    num2 = get_num2()
    result = (num1 / num2)
    set_answer(result)


button_sub = tkinter.Button(window, text = "+", command = add, width=7, height=2, bg = "white")
button_sub.place(x=105, y=110)
button_sub = tkinter.Button(window, text="-", command=sub, width=7, height=2, bg = "white")
button_sub.place(x=160, y=110)
button_multiply = tkinter.Button(
    window, text="*", command=mul, width=7, height=2, bg = "white")
button_multiply.place(x=105, y=150)
button_division = tkinter.Button(
    window, text="/", command=div, width=7, height=2, bg = "white")
button_division.place(x=160, y=150)

text_num1 = tkinter.Entry(window, width=20, bg = "white")
text_num1.place(x=95, y=40)

text_num2 = tkinter.Entry(window, width=20, bg = "white")
text_num2.place(x=95, y=81)

text_answer = tkinter.Entry(window, width=20, bg = "white")
text_answer.place(x=95, y=221)

label_num1 = tkinter.Label(window, text="Enter the first number", bg = "pink")
label_num1.place(x=95, y=20)

label_num1 = tkinter.Label(window, text="Enter the second number", bg = "pink")
label_num1.place(x=95, y=61)

label_num1 = tkinter.Label(window, text="Answer", bg = "pink")
label_num1.place(x=95, y=200)

window.configure(bg="blue")

window.mainloop()
