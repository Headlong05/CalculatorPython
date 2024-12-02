from tkinter import *
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def get_operator_symbol(self, op):
        if op == "add":
            return "+"
        elif op == "subtract":
            return "-"
        elif op == "multiply":
            return "*"
        elif op == "divide":
            return "/"
        return ""

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        try:
            self.current = float(self.current)
        except ValueError:
            self.current = 0
        if self.op_pending:
            self.basic_op()
        else:
            self.total = float(text_box.get())

        if self.op == "add":
            self.total -= self.current
        elif self.op == "subtract":
            self.total += self.current
        elif self.op == "multiply":
            self.total /= self.current
        elif self.op == "divide":
            self.total *= self.current

        if not self.get_operator_symbol(self.op):
            history_label.config(text=f"{self.total} =")
        else:
            history_label.config(text=f"{self.total} {self.get_operator_symbol(self.op)} {self.current} =")
        self.total=float(text_box.get())
        if text_box.get() == "0":
            history_label.config(text=f"{self.total} =")

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def basic_op(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "subtract":
            self.total -= self.current
        elif self.op == "multiply":
            self.total *= self.current
        elif self.op == "divide":
            self.total /= self.current
        elif self.op == "powerof":
            self.total = self.total ** 2
        elif self.op == "rootof":
            self.total = self.total ** (1 / 2)
        elif self.op == "invert":
            self.total = 1 / self.total

        history_label.config(text=f"{self.total} {self.get_operator_symbol(self.op)} {self.current}")

        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.basic_op()
        elif not self.eq:
            self.total = self.current

        history_label.config(text=f"{self.total} {self.get_operator_symbol(op)}")

        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0
        history_label.config(text="")

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

    def sqrt_func(self):
        self.current = float(text_box.get())
        result = math.sqrt(self.current)
        self.display(result)
        self.current = float(text_box.get())
    def invert_func(self):
        self.current = float(text_box.get())
        result = 1 / self.current
        self.display(result)
        self.current = float(text_box.get())

    def square_func(self):
        self.current = float(text_box.get())
        result = self.current ** 2
        self.display(result)
        self.current = float(text_box.get())

    def percent_func(self):
        self.current = float(text_box.get())
        result = self.current / 100
        self.display(result)
        self.current = float(text_box.get())

    def backspace(self):
        current_value = text_box.get()
        if len(current_value) > 0:
            new_value = current_value[:-1]
            self.display(new_value)
            if new_value:
                self.current = new_value
            else:
                self.current = "0"
        if new_value == "":
            new_value = "0"
        self.display(new_value)


sum1 = Calc()
root = Tk()
root.resizable(False, False)
calc = Frame(root)
calc.grid()

history_label = Label(calc, text="", width=24, anchor='e', font="Times 12 bold", bg="light gray")
history_label.grid(row=0, column=0, columnspan=8, padx=30, pady=(10, 0))

def operation(self, op):
    self.current = float(self.current)
    if self.op_pending:
        self.basic_op()
    elif not self.eq:
        self.total = self.current
    self.new_num = True
    self.op_pending = True
    self.op = op
    self.eq = False
    history_label.config(text=f"{self.total} {op}")


root.title("Calculator")
text_box = Entry(calc, justify=RIGHT,width=20,font="Times 16 bold")
text_box.grid(row = 1, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
button = []
for j in range(1,4):
    for k in range(3):
        button.append(Button(calc,height =2,width=6,padx=10, pady = 10, text = numbers[i]))
        button[i]["bg"]= "aliceblue"
        button[i].grid(row = j+3, column = k,padx=1,pady=1)
        button[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

backspace_button = Button(calc, height=2, width=6, padx=10, pady=10, text="←", bg="aliceblue")
backspace_button["command"] = sum1.backspace
backspace_button.grid(row=2, column=3, padx=1, pady=1)

zero_button = Button(calc,height =2,width=6,padx=10, pady = 10, text = "0",bg="aliceblue")
zero_button["command"] = lambda: sum1.num_press(0)
zero_button.grid(row = 7, column = 1,  padx=1, pady = 1)

addition = Button(calc,height =2,width=6,padx=10, pady = 10, text = "+",bg="aliceblue")
addition["command"] = lambda: sum1.operation("add")
addition.grid(row = 6, column = 3,  padx=1, pady = 1)

subtract = Button(calc,height =2,width=6,padx=10, pady = 10, text = "-",bg="aliceblue")
subtract["command"] = lambda: sum1.operation("subtract")
subtract.grid(row = 5, column = 3, padx=1, pady = 1)

multiply = Button(calc,height =2,width=6,padx=10, pady = 10, text = "*",bg="aliceblue")
multiply["command"] = lambda: sum1.operation("multiply")
multiply.grid(row = 4, column = 3,  padx=1, pady = 1)

division = Button(calc,height =2,width=6,padx=10, pady = 10, text = "/",bg="aliceblue")
division["command"] = lambda: sum1.operation("divide")
division.grid(row = 3, column = 3, padx=1, pady = 1)

square_button = Button(calc, height=2, width=6, padx=10, pady=10, text="x²", bg="aliceblue")
square_button["command"] = sum1.square_func
square_button.grid(row=3, column=1, padx=1, pady=1)

sqrt_button = Button(calc, height=2, width=6, padx=10, pady=10, text="√x", bg="aliceblue")
sqrt_button["command"] = sum1.sqrt_func
sqrt_button.grid(row=3, column=2, padx=1, pady=1)

invert_button = Button(calc, height=2, width=6, padx=10, pady=10, text="1/x", bg="aliceblue")
invert_button["command"] = sum1.invert_func
invert_button.grid(row=3, column=0, padx=1, pady=1)

dec_point = Button(calc,height =2,width=6,padx=10, pady = 10, text = ",",bg="aliceblue")
dec_point["command"] = lambda: sum1.num_press(".")
dec_point.grid(row = 7, column = 2, padx=1, pady = 1)

sign = Button(calc,height =2,width=6,padx=10, pady = 10, text = "+/-",bg="aliceblue")
sign["command"] = sum1.sign
sign.grid(row = 7, column = 0,  padx=1, pady = 1)

clear = Button(calc,height =2,width=6,padx=10, pady = 10, text = "CE",bg="aliceblue")
clear["command"] = sum1.clear
clear.grid(row = 2, column = 1,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=6,padx=10, pady = 10, text = "C",bg="aliceblue")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 2, column = 2, padx=1, pady = 1)

equals = Button(calc,height =2,width=6,padx=10, pady = 10, text = "=",bg="cadetblue4")
equals["command"] = sum1.calc_total
equals.grid(row = 7, column = 3,columnspan=1,rowspan=2,padx=1, pady = 1)

percent_button = Button(calc, height=2, width=6, padx=10, pady=10, text="%", bg="aliceblue")
percent_button["command"] = sum1.percent_func
percent_button.grid(row=2, column=0, padx=1, pady=1)

def show_info():
    info_window = Toplevel(root)
    info_window.title("Информация")
    info_window.geometry("300x200")

    label = Label(info_window, text="О программе \n ©headlong05, 2024 \n Выражаю благодарность \n Смолякову Дмитрию Геннадьевичу \n и \n Смоляковой Ольге Ивановне \n за воспитание такого прекрасного разработчика", padx=10, pady=10)
    label.pack()

    close_button = Button(info_window, text="Закрыть", command=info_window.destroy)
    close_button.pack(pady=10)

    info_window.transient(root)
    info_window.grab_set()

root.bind('<F1>', lambda event: show_info())
root.mainloop()
