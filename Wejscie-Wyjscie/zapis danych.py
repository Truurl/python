#!/usr/bin/python

password = input("Podaj hasło do zamka szyfrowego: ")

while True:
    temp_password = input("Podaj kod do zamka: ")
    if password == temp_password:
        print("Udało otworzyć się zamek")
        break
    print("Zła sekwencja, spróbuj ponownie")

