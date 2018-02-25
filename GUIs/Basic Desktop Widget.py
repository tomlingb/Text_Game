#!/usr/bin/python
import tkinter
from tkinter import ttk
import Applications.Calculator as calc


def main():
    root = tkinter.Tk()
    root.title("Desktop Helper")

    main_frame = ttk.Frame(root, padding=30, relief='raised')
    main_frame.grid()

    calculator_button = ttk.Button(main_frame, text='Calculator')
    calculator_button.grid(row=0, column=1)
    calculator_button['command'] = lambda: open_calculator()

    root.mainloop()


def open_calculator():
    calc.main()


main()
