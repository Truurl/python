#!/usr/bin/python3

import numpy as np

def generate_random_matrix(n: int, m: int):
    return np.random.rand(n, m)

def main():

    A = generate_random_matrix(8, 8)
    determinant = np.linalg.det(A)
    print(f'A = {A},\nA shape: {np.shape(A)}, A determinant: {determinant}')

if __name__ == '__main__':
    main()