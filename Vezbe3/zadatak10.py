
def main(): 
    tacka_A = {}
    tacka_B = {}

    tacka_A['x'], tacka_A['y'] = eval(input('Unesite koordinate tacke A (odvojene zarezom): '))
    tacka_B['x'], tacka_B['y'] = eval(input('Unesite koordinate tacke B (odvojene zarezom): '))

    m = (tacka_B['y'] - tacka_A['y'])/(tacka_B['x'] - tacka_A['x'])

    print('Nagib prave kroz date tacke: ', m)
    

main()