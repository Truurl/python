#!/usr/bin/python3

import numpy as np

def generate_random_matrix(n: int, m: int):
    return np.random.rand(n, m)

def main():
    A = generate_random_matrix(128, 128)
    B = generate_random_matrix(128, 128)

    C = A + B

    print(f'A = {A}, A shape: {np.shape(A)}')
    print(f'B = {B}, B shape: {np.shape(B)}')
    print(f'A + B = {C}, C shape: {np.shape(C)}')

if __name__ == '__main__':
    main()