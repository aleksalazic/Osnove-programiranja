import math

def main():
    tacka_1 = {}
    tacka_2 = {}

    tacka_1['x'], tacka_1['y'] = eval(input('Unesite koordinate tacke 1 (odvojene zarezom): '))
    tacka_2['x'], tacka_2['y'] = eval(input('Unesite koordinate tacke 2 (odvojene zarezom): '))

    d = math.sqrt((tacka_2['x'] - tacka_1['x'])**2 + (tacka_2['y'] - tacka_1['y'])**2)
    print('Rastojanje izmedju tacaka {0} i {1} je {2}'.format(tacka_1, tacka_2, d))


main()