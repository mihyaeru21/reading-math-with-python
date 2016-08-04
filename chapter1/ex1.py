# -*- coding: utf-8 -*-

def is_even(x):
    return x % 2 == 0

def print_nums(x):
    for i in range(x, x+20, 2):
        print(i)

if __name__ == '__main__':
    string = input('Input integer: ')
    num = float(string) # なぜか要件ではここの例外については触れていない
    if num.is_integer():
        num = int(num)
        print('the number is ' + ('even' if is_even(num) else 'odd'))
        print_nums(num)
    else:
        print('Invalid input')

