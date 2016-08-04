# -*- coding: utf-8 -*-

def km2miles(km):
    return km / 1.609

def miles2km(miles):
    return miles * 1.609

def kg2pound(kg):
    return kg * 2.20462

def pound2kg(pound):
    return pound / 2.20462

def celsius2fahrenheit(c):
    return c * (9 / 5) + 32

def fahrenheit2celsius(f):
    return (f - 32) * (5 / 9)

if __name__ == '__main__':
    print('1234 km    = {0:.3f} miles'.format(km2miles(1234)))
    print('1234 miles = {0:.3f} km'.format(miles2km(1234)))
    print('1234 kg    = {0:.3f} pound'.format(kg2pound(1234)))
    print('1234 pound = {0:.3f} kg'.format(pound2kg(1234)))
    print('1234 c     = {0:.3f} f'.format(celsius2fahrenheit(1234)))
    print('1234 f     = {0:.3f} c'.format(fahrenheit2celsius(1234)))

