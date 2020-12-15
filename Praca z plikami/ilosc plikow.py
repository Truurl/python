#!/usr/bin/python3

import os

PATH = '/dev'

number_of_files = sum(len(files) for root, dirs, files in os.walk(PATH))

print (f"Ilosc plikow w katalogu /dev wraz z podkatalogami: {number_of_files}")