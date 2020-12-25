from factorial.factorial import *
from exp_root.exponentiation import *
from exp_root.root import *
from logarithm.logarithm import *
import sys


def main():
    while True:
        service = input('''TYPE NUMBERS AND 'back' TO NAVIGATE
TYPE 'exit' TO EXIT
        Select option:
        1. Factorial
        2. Exponentiation
        3. Root
        4. Logarithm
        ''')
        if service == 'exit':
            sys.exit()
        if service == '1':
            while True:
                num = input('Enter natural number (type "back" to return to menu): ')
                if num == 'back':
                    break
                try:
                    num = int(num)
                except ValueError:
                    print('That`s not a natural number! Try again')
                    break
                else:
                    if int(num) < 0:
                        print('That`s not a natural number! Try again')
                        break
                    if int(num) == 0:
                        print('!', num, ' = ', 1, sep='')
                    else:
                        print('!', num, ' = ', fact(num), sep='')
        elif service == '2':
            while True:
                service2 = input('''\t\tSelect power:
                    2. 2nd
                    3. 3rd
                    ''')
                if service2 == 'back':
                    break
                elif service2 == '2':
                    while True:
                        num = input('Enter real number (type "back" to return to menu): ')
                        if num == 'back':
                            break
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            print(num, ' ^ ' + service2, ' = ', exp2(num), sep='')
                elif service2 == '3':
                    while True:
                        num = input('Enter real number (type "back" to return to menu): ')
                        if num == 'back':
                            break
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            print(num, ' ^ ' + service2, ' = ', exp3(num), sep='')
                else:
                    print('There`s no such option! Try again')
        elif service == '3':
            while True:
                service2 = input('''\t\tSelect root:
                    2. Square
                    3. Cubic
                    ''')
                if service2 == 'back':
                    break
                elif service2 == '2':
                    while True:
                        num = input('Enter real number (type "back" to return to menu): ')
                        if num == 'back':
                            break
                        if float(num) < 0:
                            print('Ypu can`t calculate a square root of a negative number! Try again')
                            continue
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            print('√', num, ' = ', root2(num), sep='')
                elif service2 == '3':
                    while True:
                        num = input('Enter real number (type "back" to return to menu): ')
                        if num == 'back':
                            break
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            if float(num) < 0:
                                num = -float(num)
                                print('∛-', num, ' = ', '-', root3(num), sep='')
                            else:
                                print('∛', num, ' = ', root3(num), sep='')
                else:
                    print('There`s no such option! Try again')
        elif service == '4':
            while True:
                service2 = input('''\t\tSelect logarithm's base:
                    1. Common logarithm log(x, 10)
                    2. Natural logarithm log(x, e)
                    3. Custom logarithm log(x, b)
                    ''')
                if service2 == '1':
                    while True:
                        num = input('log(x, 10), x: ')
                        if num == 'back':
                            break
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            if float(num) <= 0:
                                print('That  number is lower than 0! Try again')
                                continue
                            print('log(', num, ', 10) = ', lg(num), sep='')
                if service2 == '2':
                    while True:
                        num = input('log(x, e), x: ')
                        if num == 'back':
                            break
                        try:
                            num = float(num)
                        except ValueError:
                            print('That`s not a real number! Try again')
                            continue
                        else:
                            if float(num) <= 0:
                                print('That  number is lower than 0! Try again')
                                continue
                            print('log(', num, ', 10) = ', ln(num), sep='')
                if service2 == '3':
                    while True:
                        num = input('log(x, b), x: ')
                        if num == 'back':
                            break
                        base = input('log(' + num + ', b), b: ')
                        if base == 'back':
                            break
                        try:
                            num = float(num)
                            base = float(base)
                        except ValueError:
                            print('One of these is not a real number! Try again')
                            continue
                        else:
                            if float(num) <= 0 or float(base) <= 0 or float(base) == 1:
                                print('That  number is lower than 0! Try again')
                                continue
                            print('log(', num, ', ', base, ') = ', log(num, base), sep='')
                else:
                    print('There`s no such option! Try again')
        else:
            print('There`s no such option! Try again')


if __name__ == '__main__':
    main()
