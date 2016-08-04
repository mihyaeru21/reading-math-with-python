# -*- coding: utf-8 -*-

def print_nums(x, n):
    for i in range(1, n + 1):
        print('{0} x {1} = {2}'.format(x, i, x*i))

if __name__ == '__main__':
    while True:
        num = int(input('Input number: '))
        count = int(input('Input count: '))
        print_nums(num, count)

        answer = input('Do you want to exit? (y) for yes: ')
        if answer == 'y':
            break

