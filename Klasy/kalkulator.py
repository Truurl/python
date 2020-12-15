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


class Calculator:

    def __init__(self):
        self.allowed_symbols = ('+', '-', '*', '/', '(', ')', 'i', 'j', ' ')
        self.expression = ''

    def get_exxpression(self):
        return input("Wpisz działanie: ")

    def check_syntax(self, expression):

        for index, sign in enumerate(expression):
            if sign.isdigit() or sign in self.allowed_symbols:
                pass
            else:
                print(f"Zly symbol na pozycji {index}")
                return False

        self.expression = expression
        return True

    def replace_symbol_in_complex(self):
        self.expression.replace('i', 'j')

    def calculate_result(self):

        try:
            result = eval(self.expression)
            print(f"Wynik działania: {result}")
        except ZeroDivisionError:
            print("Nie można dzielić przez 0")
        except NotImplemented as not_implemented:
            print(not_implemented)

    def run(self):

        while True:
            expression = self.get_exxpression()
            if self.check_syntax(expression):
                self.replace_symbol_in_complex()
                self.calculate_result()


def main():

    calculator = Calculator()
    calculator.run()


if __name__ == '__main__':
    main()