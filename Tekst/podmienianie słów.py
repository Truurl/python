#!/usr/bin/python3

FILE_1 = 'przykladowy_tekst.txt'

strings_dict = {
    ' i ': ' oraz ',
    ' oraz ': ' i ',
    ' nigdy ': ' prawie nigdy ',
    ' dlaczego ': ' czemu '
}

with open('przykladowy_tekst.txt', 'r') as file:
    text = file.readline()

    for word, replace in strings_dict.items():
        # print(unwanted_strin, replacement_string)

        text = text.replace(replace, word)

    out = open('podmiana.txt', 'w')
    out.write(text)
    out.close()
