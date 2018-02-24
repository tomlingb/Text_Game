def main():
    while True:
        functions = ['print_file()', 'character_in_file()', 'count_char()']
        print('The available functions are:')
        for k in range(len(functions)):
            print(k, ':', functions[k])
        print('')
        print(
            '\nPlease enter the number corresponding to the desired function')
        user_input = input()
        if str(user_input) == 'quit':
            break
        user_input = int(user_input)
        user_input = functions[user_input]
        if user_input == 'print_file()':
            print_file()
        elif user_input == 'character_in_file()':
            character_in_file()
        elif user_input == 'count_char()':
            count_char()
        else:
            print('That is an invalid function')


def file():
    filename = str(input('Enter the name of the file:'))
    my_file = open(filename, 'r')
    return my_file


def print_file():
    my_file = file()
    print(my_file.read())
    my_file.close()


def character_in_file():
    my_file = file()
    user_input = input('Enter a character:')
    char = str(user_input)
    for k in my_file.read():
        if k == char:
            print('\nFile contains the character', char, '\n')
            break


def count_char():
    count = 0
    my_file = file()
    char_input = str(input('Input a number or letter:'))
    for c in my_file.read():
        if c == char_input:
            count += 1
    print('\n',
          'The character ' + char_input + ' appears ' + str(count) + ' times',
          '\n')


main()
