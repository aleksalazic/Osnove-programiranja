
fajl = open('podaci.txt', 'a')

korisnicko_ime = input('Unesite korisnicko ime: ')
lozinka = input('Unesite lozinku: ')

print('{0}|{1}'.format(korisnicko_ime, lozinka), file=fajl)

fajl.close()