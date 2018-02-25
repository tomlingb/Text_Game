#!/usr/bin/python
import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()
    root.title('Calculator')

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    calc_input = ttk.Entry(main_frame, width=20)
    calc_input.grid(row=1, column=0)

    solution = ttk.Label(main_frame, text='')
    solution.grid(row=2, column=0)

    previous_equation = ttk.Label(main_frame, text='')
    previous_equation.grid(row=0, column=0)

    exit_button = ttk.Button(main_frame, text='Exit')
    exit_button.grid(row=0, column=2)
    exit_button['command'] = lambda: exit_program()

    calculate = ttk.Button(main_frame, text='Calculate')
    calculate.grid(row=1, column=1)
    calculate['command'] = lambda: calculator(list(calc_input.get()), solution, calc_input, previous_equation)
    root.bind('<Return>', lambda event: calculator(list(calc_input.get()), solution, calc_input, previous_equation))

    root.mainloop()


'''def main():
    while True:
        get_input()'''


def calculator(command, solution_text, input_box, previous_equation):
    value = 0
    power_finished = False
    while power_finished is False:
        power_count = 0
        for k in range(len(command)):
            if command[k] == '*' and command[k + 1] == '*':
                power_count += 1
        print(command)
        print('power count:', power_count)
        if power_count > 0:
            power_complete = False
            while power_complete is False:
                for k in range(len(command)):
                    if command[k] == '*' and command[k + 1] == '*':
                        value = power(command[k - 1], command[k + 2])
                        index = k
                        power_complete = True
                        break
            del command[index + 2]
            del command[index + 1]
            command[index] = value
            del command[index - 1]
        if power_count == 0:
            print(command)
            power_finished = True
    mult_finished = False
    while mult_finished is False:
        mult_count = 0
        for k in range(len(command)):
            if command[k] == '*':
                mult_count += 1
        print(command)
        print('mult count:', mult_count)
        if mult_count > 0:
            mult_complete = False
            while mult_complete is False:
                for k in range(len(command)):
                    if command[k] == '*':
                        value = multiply(command[k - 1], command[k + 1])
                        index = k
                        mult_complete = True
                        break
            del command[index + 1]
            command[index] = value
            del command[index - 1]
        if mult_count == 0:
            print(command)
            mult_finished = True
    div_finished = False
    while div_finished is False:
        div_count = 0
        for k in range(len(command)):
            if command[k] == '/':
                div_count += 1
        print(command)
        print('div count:', div_count)
        if div_count > 0:
            div_complete = False
            while div_complete is False:
                for k in range(len(command)):
                    if command[k] == '/':
                        value = divide(command[k - 1], command[k + 1])
                        index = k
                        div_complete = True
                        break
            del command[index + 1]
            command[index] = value
            del command[index - 1]
        if div_count == 0:
            print(command)
            div_finished = True
    add_finished = False
    while add_finished is False:
        add_count = 0
        for k in range(len(command)):
            if command[k] == '+':
                add_count += 1
        print(command)
        print('add count:', add_count)
        if add_count > 0:
            add_complete = False
            while add_complete is False:
                for k in range(len(command)):
                    if command[k] == '+':
                        value = add(command[k - 1], command[k + 1])
                        index = k
                        add_complete = True
                        break
            del command[index + 1]
            command[index] = value
            del command[index - 1]
        if add_count == 0:
            print(command)
            add_finished = True
    subtract_finished = False
    while subtract_finished is False:
        subtract_count = 0
        for k in range(len(command)):
            if command[k] == '-':
                subtract_count += 1
        print(command)
        print('subtract count:', subtract_count)
        if subtract_count > 0:
            subtract_complete = False
            while subtract_complete is False:
                for k in range(len(command)):
                    if command[k] == '-':
                        value = subtract(command[k - 1], command[k + 1])
                        index = k
                        subtract_complete = True
                        break
            del command[index + 1]
            command[index] = value
            del command[index - 1]
        if subtract_count == 0:
            print(command)
            subtract_finished = True
    if len(command) == 1:
        solution = command[0]
        solution_text.configure(text=solution)
        previous_equation.configure(text=input_box.get())
        input_box.delete(0, 9999)
    else:
        error_msg = 'something went wrong'
        solution_text.configure(text=error_msg)


def add(first, second):
    value = float(first) + float(second)
    return value


def subtract(first, second):
    value = float(first) - float(second)
    return value


def multiply(first, second):
    value = float(first) * float(second)
    return value


def divide(first, second):
    value = float(first) / float(second)
    return value


def power(first, second):
    value = float(first) ** float(second)
    return value


def exit_program():
    quit()


main()
