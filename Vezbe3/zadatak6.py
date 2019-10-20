import math

def main():
    r = float(input('Unesite poluprecnik pice: '))
    cena = float(input('Unesite cenu pice: '))

    povrsina_pice = r**2 * math.pi

    print('Cena po kvadratnom centimetru: {}'.format(povrsina_pice/cena))


main()