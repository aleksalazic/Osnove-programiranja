


def main():
    suma = 0
    imenilac = 1
    n = int(input('Unesite ceo broj: '))
    
    for i in range(1, n+1):
        
        if i % 2 != 0:
            suma += 4/imenilac
            imenilac += 2
        else:
            suma -= 4/imenilac
            imenilac += 2

    print('Pi: {}'.format(suma))







main()