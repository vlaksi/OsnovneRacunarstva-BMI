import math
import sys

def main():
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        disc = b * b - 4 * a * c
        if disc > 0:
            discRoot = math.sqrt(b * b - 4 * a * c)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print("\nThe solutions are:", root1, root2)
        elif disc == 0:
            root = (-b) / (2 * a)
            print("\nThe solution is:", root)
        else:
            # print()
            print('\nThere are no solutions')
    except ValueError as err:
        if 'not enough values to unpack' in str(err):
            print('nije uneto dovoljno vrednosti!')
        elif 'too many values to unpack' in str(err):
            print('uneto previse vrednosti!')
        else:
            print(err)
    except NameError:
        print('vrednosti moraju biti brojevi')
    except SyntaxError:
        print('moraju se uneti vrednosti')
    except ZeroDivisionError:
        print('parametar a ne sme biti 0')


main()