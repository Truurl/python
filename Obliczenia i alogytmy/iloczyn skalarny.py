#!/usr/bin/python3

import numpy as np

vector_1 = np.array([1, 2, 12, 4])
vector_2 = np.array([2, 4, 2, 8])

result = np.dot(vector_1, vector_2)

print(f'Wynik iloczynu skalarnego dwóch wektoróe {vector_1} i {vector_2} = {result}')