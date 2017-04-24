#!/usr/bin/env python
# coding: UTF-8
#
## @package Mileage Calculator
#
#   Class for reading a series of odometer and gallons data
#   from filling up the gas tak of a vehicle, and calculating
#   the consumption between each gas station stop.
#
# @author paulo Roma
# @date 24/08/2014
#


import sys


class FillUp:
    ##
    # Odometer reading when the tank was filled
    #
    odometer = 0.0

    ##
    # Gallons needed to fill the tank
    #
    gallons = 0.0

    ##
       # Construcs a new FillUp object with the given data.
       # @param given_odometer
       #   odometer reading
       # @param given_gallons
       #   number of gallons
       #
    def __init__(self, given_odometer, given_gallons):
        self.odometer = given_odometer
        self.gallons = given_gallons

    ##
       # Returns the odometer reading.
       # @return
       # the odometer reading
       #
    def get_odometer(self):
        return self.odometer

    ##
       # Returns number of gallons.
       # @return
       # number of gallons
       #
    def get_gallons(self):
        return self.gallons


class MileageCalculator:

    ### fillup list, which aggregates two values.
    fillup = []

    ### debugging state
    debug = False

    ##
    #   Constructor
    #   Opens filename and calls Reader for inputting the mileage reader
    #   Raises an exception if filename does not exist.
    #
    #   @param filename mileage file name
    #
    def __init__(self, filename):
        try:
            file = open(filename, 'r')
        except IOError:
            print('Cannot open file {} for reading'.format(filename))
            raise
        self.reader(file)

    ##
    #   Reads a file with mileage and gasoline per line.
    #   Creates FillUp objects for each line and inserts in the fillup list.
    #
    #   @param file mileage file object.
    #
    def reader(self, file):
        for line in file:
            temp_words = line.split()
            if len(temp_words) == 2:
                try:
                    self.fillup.append(FillUp(float(temp_words[0]), float(temp_words[1])))
                except:
                    print('Invalid reading {}'.format(temp_words))
        file.close()

    ##
    #   Calculates the consuption of the k-th of fillup list.
    #
    #   @param k fillup index
    #   @return (odometer[k] - odometer[k-1])/gallons[k].
    #
    def consuption(self, k):
        if k < 1 or k >= len(self.fillup):
            return ""

        previous = self.fillup[k-1].get_odometer()
        current = self.fillup[k].get_odometer()
        gallons = self.fillup[k].get_gallons()

        if MileageCalculator.debug:
            print("current {0}\nprevious {1}\ngallons{2}".format(current, previous,gallons))

        return (current - previous) / gallons

    ##
    #   Returns the consuption (in mi/gal) correspoding to each
    #   entry of "fillup", by calling the method "consuption".
    #
    #   @return a string: a series of consuptions.
    #
    def __repr__(self):
        sb = "Miles per gallon\n"
        for i in range(1, len(self.fillup)):
            sb += "Consump. {0}: {1:3f}\n".format(i, self.consuption(i))

        return sb

    ##
    #   Returns the consuption (in km/lt) corresponding to each entry
    #   of "fillup", by calling the method "consuption".
    #
    #   1 gallon = 3.7853118
    #
    #   1 mile = 1.609344
    #
    #   @return a string: a series of consuptions.
    #
    def __str__(self):
        sb = "Kilometers per litre\n"
        for i in range(1, len(self.fillup)):
            sb += "Consump. {0}: {1:3f}\n".format(i, self.consuption(i) * 1.609344 / 3.7854118)

        return sb


##
#   Main method. Reads a series of pairs of mileage and number of
#   the average consumption: (current - previous)/gallons.
#
def main(argv=None):
    f = "mileage.txt"
    d = False
    if argv is None:
        argv = sys.argv

    if (len(argv) > 2):
        f = argv[1]
        d = argv[2] == 'True'

    try:
        m = MileageCalculator(f)
        MileageCalculator.debug = d
        print(m)
        print(repr(m))
    except IOError:
        sys.exit("File {} not found".format(f))


if __name__ == '__main__':
    sys.exit(main())
