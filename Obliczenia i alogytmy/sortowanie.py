#!/usr/bin/python3

import random
import copy



def main():
    random_list = [random.randint(0, 1000) for x in range(0, 50)]
    print(f'Losowa lista 50 elementowa:\n{random_list}')

    sorted_list = copy.copy(random_list)
    for iter in range(0, len(sorted_list) - 1):
        current_value = sorted_list[iter]
        j = iter + 1
        while True:
            if j == len(sorted_list):
                break
            if current_value < sorted_list[j]:
                sorted_list[iter] = sorted_list[j]
                sorted_list[j] = current_value
                current_value = sorted_list[iter]
                j = iter + 1
            j += 1

    print(f'Sortowanie za pomocą wlasnej funkcji: {sorted_list}')
    print(f'Sortowanie za pomocą wbudowanej funkcji: {sorted(random_list, reverse=True)}')
    print(f'Wynik porównania dwóch metod sortowania: {sorted(random_list, reverse=True) == sorted_list}')

if __name__ == '__main__':
    main()
