#!/usr/bin/env python
# coding: UTF-8
#
## @package _01a_fracao
#
# A very simple fraction class;
#
# @author Miguel Jonathan e Paulo Roma
# @since 16/09/2009
# @see http://docs.python.org/libraary/fractions.html
# @see http://docs.python.org/reference/datamodel.emulating-num

## A simple class for creating fraction objects (rational numbers).


import sys


class Fracao:
    ## Constructor
    #
    # @param num numerator
    # @param den denominator
    #
    def __init__(self, num=1, den=1):
        """Constructor"""

        if den == 0: raise ValueError("Zero deniminator")

        ### Numerator.
        self.num = num
        ### Denominator.
        self.den = den

        if self.den < 0:  # check for a negative denominator
            self.num = -self.num  # change the signal of the numarator
            self.den = -self.den
        self.simplifica()

    def simplifica(self):
        larger = 1
        if self.num != 0:  # assert Fracao != 0
            larger = mdc(self.num, self.den)  # find the gdc
        if larger > 1:  # reduce this fraction
            self.num //= larger  # integer division
            self.den //= larger
        return self

    def __eq__(self, other):
        a = self.simplifica()
        b = other.simplifica()
        return a.num == b.num and a.den == b.den

    ## Operator +
    #
    def __add__(self, other):
        if isinstance(other, int):          # check other is integer
            num = self.num + other * self.den
            den = self.den
        elif isinstance(other, Fracao):     # check other is fraction
            den = self.den * other.den
            num = self.num * other.den + self.den * other.num
        else:
            raise TypeError("__add__")
        # returns a copy, and therefore is slower
        return Fracao(num, den)             # Fraction is simplified

    ## Operator +=
    #
    def __iadd__(self, other):
        if isinstance(other, int):          # check other is integer
            self.num += other * self.den
        elif isinstance(other, Fracao):     # check other is fraction
            self.num = self.num * other.den + self.den * other.num
            self.den *= other.den
        else:
            raise TypeError("__iadd__")
        return self.simplifica()            # Fraction is simplified

    ## Operator -
    #
    def __sub__(self, other):
        if isinstance(other, int):          # check other is an integer
            num = self.num - other * self.den
            den = self.den
        elif isinstance(other, Fracao):     # check other is a fraction
            den = self.den * other.den
            num = self.num * other.den - self.den * other.num
        else:
            raise TypeError("__sub__")
        return Fracao(num, den)

    ## Operator *
    #
    def __mul__(self, other):
        if isinstance(other, int):          # check other is an integer
            num = self.num * other
            den = self.den
        elif isinstance(other, Fracao):     # check other is a fraction
            num = self.num * other.num
            den = self.den * other.den
        else:
            raise TypeError("__mul__")
        return Fracao(num, den)

    ## Operator /
    #
    def __truediv__(self, other):
        if isinstance(other, int):          # check other is an integer
            num = self.num
            den = self.den * other
        elif isinstance(other, Fracao):
            num = self.num * other.den
            den = self.den * other.num
        else:
            raise TypeError("__truediv__")
        return Fracao(num, den)

    ## Controls how a fraction is printed.
    #
    # @return a string: numerator/denominator, or
    # only the numerator, if the denominator is 1, after simple
    # 0, if the numerator is null.
    def __str__(self):
        if self.num == 0:
            return "0"
        elif self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + '/' + str(self.den)



## mdc is a general use function, defined outside the class.
#
# @param x fist integer: numerator.
# @param y second integer: denominator.
# @return GCD: Greatest Common Divisor.
#
def mdc(x, y):
    """Greatest Common Divisor (Maximo divisor comum)."""
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x


def main():
    f = Fracao(15, 45)
    g = Fracao(50, 75)
    print("f = 15/45 = %s" % f, end="\n")
    print("g = 50/75 = %s" % g, end="\n")
    print("f + g = %s" % (f + g), end="\n")
    h = Fracao(10, 28)
    print("h = 10/28 = %s" % h, end="\n")
    print("f * h = %s" % (f * h), end="\n")
    print("f + g + h = %s" % (f + g + h), end="\n")
    print("f + g * h = %s" % (f + g * h), end="\n")
    print("g - f - f = %s" % (g - f - f), end="\n")
    print("f * 2 = %s" % (f * 2), end="\n")
    print("f + 2 = %s" % (f + 2), end="\n")
    print("f / g = %s" % (f / g), end="\n")
    f += g * 2
    print("f += g * 2 = %s" % f, end="\n")
    f -= g * 2
    print("f -= g * 2 = %s" % f, end="\n")

    try:
        print("2 + f = ", 2 + f)
    except (ValueError, TypeError) as e:
        print("Exception caught: %s" % e, end="\n")

    print("f == h %s" % (f == h), end="\n")
    print("f = g = h")
    f = g = h
    print("f == g %s" % (f == h), end="\n")

    try:
        print("f += \'a\'")
        f += "a"
    except (ValueError, TypeError) as e:
        print("Exception caught: %s" % e, end= "\n")

    try:
        print("Fracao(2, 0) = ")
        print(Fracao(2, 0))
    except (ValueError, TypeError) as e:
        print("Exception caught: %s" % e, end="\n")

if __name__ == "__main__":
    sys.exit(main())
