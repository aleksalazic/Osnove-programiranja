
def ispisi_knjige(lista_knjiga):
    print('{0:<5}{1:<20}{2:<25}{3:<25}{4:<15}{5:<15}{6:<15}'.format('id', 'naslov', 'autori', 'izdavac', 'cena', 'kolicina', 'godina'))
    print(112*'-')
    for knjiga in lista_knjiga:
        print('{0:<5}{1:<20}{2:<25}{3:<25}{4:<15}{5:<15}{6:<15}'.format(knjiga['id'], knjiga['naslov'], knjiga['autori'], knjiga['izdavac'], knjiga['cena'], knjiga['kolicina'], knjiga['godina']))



def napravi_knjigu(iden, naslov, autori, izdavac, cena, kolicina, godina):
    knjiga = {}
    knjiga['id'] = iden
    knjiga['naslov'] = naslov
    knjiga['autori'] = autori
    knjiga['izdavac'] = izdavac
    knjiga['cena'] = cena
    knjiga['kolicina'] = kolicina
    knjiga['godina'] = godina

    return knjiga



def main():

    lista_knjiga = []


    while True:
        try:
            naslov = input('Unesite naslov knjige: ')
            autori = input('Unesite autore knjige: ')
            izdavac = input('Unesite izdavaca knjige: ')
            cena = int(input('Unesite cenu knjige: '))
            kolicina = int(input('Unesite kolicinu knjiga: '))
            godina = int(input('Unesite godinu izdanja: '))

            if len(lista_knjiga) == 0:
                lista_knjiga.append(napravi_knjigu(1, naslov, autori, izdavac, cena, kolicina, godina))
            else:
                lista_knjiga.append(napravi_knjigu(len(lista_knjiga) + 1, naslov, autori, izdavac, cena, kolicina, godina))

            ponovo = input('Da li zelite da uneste jos knjiga?(da/ne)')
            if ponovo == 'ne':
                break
        except ValueError:
            print('Cena, kolicina i godina moraju biti broj...')
        

    ispisi_knjige(lista_knjiga)




main()