def encode_decode(encoding, decoding):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    encoded_alphabet = []
    while True:
        keyword = str(input('Enter keyword: '))
        if keyword == 'quit':
            break
        keyword = list(keyword)
        for k in range(len(keyword)):
            encoded_alphabet.append(keyword[k])
        for k in range(26):
            if alphabet[k] not in encoded_alphabet:
                encoded_alphabet.append(alphabet[k])
        print(alphabet)
        print(encoded_alphabet)
        filename = str(input('Please enter the name of the file: '))
        my_file = open(filename, 'r')
        info_to_encode = my_file.read()
        my_file.close()
        print(info_to_encode)
        info_list = list(info_to_encode)
        print(info_list)
        my_file = open(filename, 'w')
        for k in range(len(info_list)):
            if info_list[k] != '\n' and info_list[k] != ' ':
                index = alphabet.index(info_list[k])
                info_list[k] = encoded_alphabet[index]
        print(info_list)
        encoded_info = ''.join(info_list)
        print(encoded_info)
        my_file.write(encoded_info)
        my_file.close()
    while True:


encode_decode(True, False)
