#!/usr/bin/env python
# codding: UTF-8
## @package _01e_fracoes
#
# Reads a file with a series of fractions, and prints their sum
# and product.
#
# @author Paulo Roma
# @since 25/09/2014


import sys

from _01a_fracao import Fracao


class Fracoes:
    ##
    #   Constructor.
    #   Opens filename and calls Reader for input the fraction readings.
    #   Raises an exception if filename does not exist
    #
    #   @param filename
    #
    def __init__(self, filename):
        ### lfracoes - a list of objects of type Fracao
        self.lfracoes = []

        try:
            f = open(filename, 'r')
        except IOError:
            print('Fracoes: Cannot open file %s for reading' % filename)
            raise
        self.Reader(f)

    def Reader(self, f):
        for line in f:
            temp = line.split(None)
            if len(temp) == 2:
                try:
                    self.lfracoes.append(Fracao(int(temp[0]), int(temp[1])))
                except:
                    print('Fração inválida: %s\n' % temp)
                    continue
        f.close()

    def __str__(self):
        sb = ""
        f = Fracao(0, 1)
        g = Fracao(1, 1)
        for i in range(0, len(self.lfracoes)):
            f += self.lfracoes[i]
            g *= self.lfracoes[i]
        sb += "Soma: %s\nProduto: %s\n" % (f, g)

        return sb

    def __repr__(self):
        sb = ""
        for i in range(0, len(self.lfracoes)):
            sb += "Fracao %d: %s\n" % (i, self.lfracoes[i])

        return sb


def main(argv=None):
    f = "fracoes.txt"
    if argv is None:
        argv = sys.argv

    if len(argv) > 1:
        f = argv[1]

    try:
        m = Fracoes(f)
        print(repr(m))
        print(m)
    except IOError:
        sys.exit("File %s not found." % f)


if __name__ == '__main__':
    sys.exit(main())
