def main():
    while True:
        get_input()


def get_input():
    command = input(':').split()
    attempt2(command)


def order_of_operations(command):
    value = 0
    op_number = 0
    op_happened = False
    for k in range(len(command)):
        if command[k] == '^' and op_happened is False:
            first = command[k - 1]
            second = command[k + 1]
            value += power(first, second)
            op_happened = True
    for k in range(len(command)):
        if command[k] == '*':
            first = command[k - 1]
            second = command[k + 1]
            value += multiply(first, second)
    for k in range(len(command)):
        if command[k] == '/':
            if op_happened is False:
                first = command[k - 1]
                second = command[k + 1]
                value += divide(first, second)
                op_happened = True
            else:
                second = command[k + 1]
                value = divide(value, second)
    for k in range(len(command)):
        if command[k] == '+':
            if op_happened is False:
                first = command[k - 1]
                second = command[k + 1]
                value += add(first, second)
                op_happened = True
            else:
                second = command[k + 1]
                value = add(value, second)
    for k in range(len(command)):
        if command[k] == '-':
            if op_happened is False:
                first = command[k - 1]
                second = command[k + 1]
                value += subtract(first, second)
                op_happened = True
            else:
                second = command[k + 1]
                value = subtract(value, second)
    print(value)


def attempt2(command):
    value = 0
    finished = False
    while finished is False:
        mult_count = 0
        for k in range(len(command)):
            if command[k] == '*':
                mult_count += 1
        print(command)
        if mult_count > 0:
            mult_complete = False
            while mult_complete is False:
                for k in range(len(command)):
                    if command[k] == '*':
                        value = multiply(command[k - 1], command[k + 1])
                        index = k
                        mult_complete = True
            command.remove(command[index + 1])
            command[index] = value
            command.remove(command[index - 1])
        if len(command) == 1:
            print(command)
            break


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


main()
