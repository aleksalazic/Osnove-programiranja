import math

def main():
    r = float(input('Unesite poluprecnik: '))

    v = (4/3)*r**3*math.pi
    p = 4*math.pi*r**2

    print('Zapremina: {0}\nPovrsina: {1}'.format(v, p))


main()