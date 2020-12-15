#!/usr/bin/python3

import os

PATH = './testowe_drzewo'

def catalog_tree_scan(dir: str, level=1):

    files_list = os.listdir(dir)

    if level==1:
        print(f'{dir}')

    for name in files_list:
        if os.path.isdir(f'{dir}/{name}'):
            print(f'{4 * level * " "}/{name}')
            catalog_tree_scan(f'{dir}/{name}', level=level+1)
        else:
            print(f'{4 * level * " "}{name}')


def main():
    catalog_tree_scan(PATH)

if __name__ == '__main__':
    main()

