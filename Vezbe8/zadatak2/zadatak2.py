def upis_u_fajl(lista_knjiga, fajl):
    knjige_fajl = open(fajl, 'w')
    for knjiga in lista_knjiga:
        print('{0}|{1}|{2}|{3}|{4}|{5}|{6}'.format(knjiga['id'], knjiga['naslov'], knjiga['autori'], knjiga['izdavac'], knjiga['cena'], knjiga['kolicina'], knjiga['godina']), file=knjige_fajl)
    knjige_fajl.close()


def citaj_iz_fajla(fajl):
    lista_knjiga = []
    knjige_fajl = open(fajl, 'r')
    for line in knjige_fajl:
        knjiga_podaci = line.strip().split('|')
        knjiga = napravi_knjigu(knjiga_podaci[0], knjiga_podaci[1], knjiga_podaci[2], knjiga_podaci[3], knjiga_podaci[4], knjiga_podaci[5], knjiga_podaci[6])
        lista_knjiga.append(knjiga)
    knjige_fajl.close()
    return lista_knjiga




def ispisi_knjige(lista_knjiga):
    print('{0:<5}{1:<20}{2:<25}{3:<25}{4:<15}{5:<15}{6:<15}'.format('id', 'naslov', 'autori', 'izdavac', 'cena', 'kolicina', 'godina'))
    print(112*'-')
    for knjiga in lista_knjiga:
        if len(knjiga['naslov']) >= 20:
            knjiga['naslov'] = knjiga['naslov'][0:16] + '...'
        print('{0:<5}{1:<20}{2:<25}{3:<25}{4:<15}{5:<15}{6:<15}'.format(knjiga['id'], knjiga['naslov'], knjiga['autori'], knjiga['izdavac'], knjiga['cena'], knjiga['kolicina'], knjiga['godina']))



def napravi_knjigu(id, naslov, autori, izdavac, cena, kolicina, godina):
    knjiga = {}
    knjiga['id'] = id
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
        


    upis_u_fajl(lista_knjiga, 'knjige.txt')
    ispisi_knjige(citaj_iz_fajla('knjige.txt'))




main()