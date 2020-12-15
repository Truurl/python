#!/usr/bin/python

import math

class Complex:

    def __init__(self, real: float, imag: float):
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,\
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ++ 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag**2)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __repr__(self):
        return  self. __str__()

    def __eq__(self, other):
        return ( self.real == other.real and self.imag == other.imag)

    def __eq__(self, other):
        return ( self.real == other.real and self.imag == other.imag)

def main():

    c1 = Complex(1.0, 2.0)
    c2 = Complex(1.0, -2.0)

    print(f'c1 = {c1}\t\tc2 = {c2}')
    print(f'Dodawanie: c1 + c2 = {c1 + c2}')
    print(f'Odejmowanie: c1 + c2 = {c1 - c2}')
    print(f'Mnożenie: c1 * c2 = {c1 * c2}')
    print(f'Dzielenie: c1 / c2 = {c1 / c2}')
    print(f'c1 == c2: {c1 == c2}')
    print(f'|c1| = {abs(c1)}')


if __name__ == '__main__':
    main()