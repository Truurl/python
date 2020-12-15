#!/usr/bin/python3

import csv
import os

def add_record():

    print("Dodawanie albumów do listy")

    row_id = 0
    with open('album_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        # print(csv_reader)
        for row in csv_reader:
            if len(row) > 0:
                row_id += 1

    with open('album_list.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')

        if row_id == 0:
            csv_writer.writerow(["Id", "Artist", "Title", "Release date", "Genre", "Rating"])
            row_id += 1

        record_dict = {
            "Id": row_id,
            "Artist": "",
            "Title": "",
            "Release date": "",
            "Genre": "",
            "Rating": ""
        }
        for key in record_dict:

            if key == "Id":
                continue

            while True:
                temp_input = input(f"Podaj wartość dla {key}: ")
                if ',' in temp_input:
                    print("Symbol ',' nie może zawierać się w wartośći.")
                else:
                    record_dict[key] = temp_input
                    break

        for key in record_dict:
            print(f'{key}: {record_dict[key]}')

        while True:
            output = input('Czy dane się zgadzają? Wpisz y/n: ')
            if output == 'y':
                row = (record_dict[key] for key in record_dict)
                csv_writer.writerow(row)
                break
            elif output == 'n':
                break
            else:
                print("Symbol musi byc 'y' lub 'n'")


def read_data():

    print(30 * "-")

    with open('album_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        record_dict = {
            "Id": "",
            "Artist": "",
            "Title": "",
            "Release date": "",
            "Genre": "",
            "Rating": ""
        }

        repeats = 0
        for row in csv_reader:
            if repeats == 0:
                repeats += 1
                continue
            print(30 * "#")
            iterator = 0;
            for key in record_dict:
                print(f"{key}: {row[iterator]}")
                iterator += 1
            print(30 * "#")
            repeats += 1


def remove_record():

    print("Dodawanie albumów do listy")

    row_amount = 0
    with open('album_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        # print(csv_reader)
        for row in csv_reader:
            if len(row) > 0:
                row_amount += 1

    with open('album_list.csv', 'r') as csv_file_read, open('album_list_temp.csv', 'w') as csv_file_write:
        csv_reader = csv.reader(csv_file_read, delimiter=',', quotechar='"')
        csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"')
        row_id = 0
        while True:
            temp_input = input(f"Podaj wartość Id wspisu, którą chcesz usunąć: ")
            if temp_input.isdigit():
                row_id = int(temp_input)
                break
            else:
                print("Id musi być liczbą dodatnią.")

        if 0 < row_id <= row_amount:
            repeats = 0
            for row in csv_reader:
                if repeats == 0:
                    csv_writer.writerow(row)
                    repeats += 1
                    continue
                elif int(row[0]) == row_id:
                    repeats += 1
                    continue
                elif repeats > row_id:
                    row[0] = str(repeats - 1)

                csv_writer.writerow(row)
                repeats += 1

    with open('album_list_temp.csv', 'r') as csv_file_read, open('album_list.csv', 'w') as csv_file_write:
        csv_reader = csv.reader(csv_file_read, delimiter=',', quotechar='"')
        csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"')

        for row in csv_reader:
            csv_writer.writerow(row)

    os.remove('album_list_temp.csv')


def main():

    print(os.path.exists("album_list.csv"))



    while True:

        print("----Co chcesz zrobić z plikiem?----")
        print("\t1) Dodaj wpis do csv")
        print("\t2) Usuń wpis z csv")
        print("\t3) Odczytaj plik csv")
        print("\t4) Wyjdź z programu")

        sign = input("Podaj opcje: ")

        if sign == '1':
            if not os.path.exists("album_list.csv"):
                open('album_list.csv', 'x')
            add_record()
        elif sign == '2':
            remove_record()
        elif sign == '3':
            read_data()
        elif sign == '4':
            break
        else:
            print("Symbol musi być liczbą od 1 do 4")

if __name__ == '__main__':
    main()