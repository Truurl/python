#!/usr/bin/python

FILE_1 = 'przykladowy_tekst.txt'

unwanted_strings = [' się ', ' i ', ' oraz ', ' nigdy ', ' dlaczego ']

with open('przykladowy_tekst.txt', 'r') as file:
    text = file.readline()

    for string in unwanted_strings:
        text = text.replace(string, ' ')

    out = open('usuwanie.txt', 'w')
    out.write(text)
