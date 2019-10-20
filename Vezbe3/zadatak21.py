import math


def main():
    x = int(input('Unesite broj: '))

    guess = x/2

    while(True):
        if abs(guess - math.sqrt(x)) > 0.000001:
            guess = (guess + x/guess)/2
        else:
            break
    
    print('Koren iz broja {0} je: {1}'.format(x, guess))



main()