def main():
    while True:
        get_input()


def get_input():
    command = input(':').split()
    print(command)
    value = 0
    op_number = 0
    for k in range(len(command)):
        if command[k] in function_list:
            first = float(command[k - 1])
            second = float(command[k + 1])
        if command[k] == '+':
            if op_number == 0:
                value += add(first, second)
                op_number += 1
            elif op_number > 0:
                value = add(value, second)
        elif command[k] == '-':
            if op_number == 0:
                value += subtract(first, second)
                op_number += 1
            elif op_number > 0:
                subtract(value, second)
        elif command[k] == '*':
            if op_number == 0:
                value += multiply(first, second)
                op_number += 1
            elif op_number > 0:
                multiply(value, second)
        elif command[k] == '/':
            if op_number == 0:
                value += divide(first, second)
                op_number += 1
            elif op_number > 0:
                divide(value, second)
        elif command[k] == '^':
            if op_number == 0:
                value += power(first, second)
                op_number += 1
            elif op_number == 1:
                value = power(value, second)
        else:
            value = 'there is no appropriate function in that command.'
    print(value)


def add(first, second):
    value = first + second
    return value


def subtract(first, second):
    value = first - second
    return value


def multiply(first, second):
    value = first * second
    return value


def divide(first, second):
    value = first / second
    return value


def power(first, second):
    value = first ** second
    return value


function_list = ['+', '-', '*', '/', '^']

main()
