def prvi_drugi_string():
    prvi_string = input('Unesite prvi string: ')
    drugi_string = input('Unesite drugi string: ')

    print(prvi_string + drugi_string)




def akronim(string):
    akronim = ''
    lista =[]
    lista = string.split(' ')
    for rec in lista:
        akronim += rec[0].upper()
    
    return akronim


def main():
    while(True):
        print('1. Konkatonacija stringova\n2. Akronim\n0. Izlaz iz programa\n')
        try:
            opcija = int(input('Unesi opciju: '))
            if opcija == 1:
                prvi_drugi_string()
            elif opcija == 2:
                string = input('Unesite frazu za akronim: ')
                print(akronim(string))
            elif opcija == 0:
                print('Program se gasi')
                break
            else:
                print('Opcija mora biti jedna od navedenih!')

        except ValueError:
            print('Opcija mora biti broj!')


main()



