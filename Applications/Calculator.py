def divide_by_0():
    print('Division by 0 is invalid')
    num2 = float(input('Please enter a new number:'))
    if num2 == 0:
        num2 = divide_by_0()
    return num2


def calculator():
    while True:
        user_input = str(input('Input function here:'))

        value = 0

        if user_input == 'add':
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
            value += num1 + num2

            print('\n The answer is:', value, '\n')

        elif user_input == 'subtract':
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
            value += num1 - num2

            print('\n The answer is:', value, '\n')

        elif user_input == 'multiply':
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
            value += num1 * num2

            print('\n The answer is:', value, '\n')

        elif user_input == 'divide':
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number:'))
            if num2 == 0:
                num2 = divide_by_0()
            value += num1 / num2

            print('\n The answer is:', value, '\n')

        elif user_input == 'quit':
            break

        else:
            print('\n Invalid Input\n')
            continue


calculator()
