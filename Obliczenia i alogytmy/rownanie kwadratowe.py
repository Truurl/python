#!/usr/bin/python3

from math import sqrt


class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real} + {self.imag}i'

    def __repr__(self):
        return f'{self.real} + {self.imag}i'


def calculate_discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def calculate_roots(a, b, c, delta):

    if delta > 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        return -b / (2 * a)
    elif delta < 0:
        x1 = Complex(-b / (2 * a), sqrt(-delta)/(2 * a))
        x2 = Complex(-b / (2 * a), -sqrt(-delta)/(2 * a))
        return x1, x2


def main():

    a, b, c = (float(x) for x in input("Podaj współczynniki równania kwadratowego: ").split())
    delta = calculate_discriminant(a, b, c)
    roots = calculate_roots(a, b, c, delta)
    print(f'Miejsca zerowe równania kwadratowego: {roots}')


if __name__ == '__main__':
    main()
