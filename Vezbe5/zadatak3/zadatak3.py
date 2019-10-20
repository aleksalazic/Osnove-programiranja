# Zadatak 3. Napiši funkciju koja čita iz fajla korisnička imena i lozinke i pročitane vrednosti vraća kao
# listu. Prilikom poziva funkcije prosleđuje se naziv fajla i delimiter kojim je u fajlu korisničko ime odvojeno
# od lozinke. Pri tome je element liste koja se vraća lista u kojoj je prvi element korisničko ime, a drugi
# element lozinka.
# Primer izvršavanja programa:
# Za fajl korisnici.txt
# pera|peric
# jova|jovic
# steva|stevic
# rezultat poziva funkcije treba da bude:
# >>> print(citanjeIzFajla("korisnici.txt","|"))
# [['pera', 'peric'], ['jova', 'jovic'], ['steva', 'stevic']]


def citaj_fajl(naziv_fajla, delimiter):
    lista_korisnika = []
    korisnici = open(naziv_fajla, 'r')
    for line in korisnici:
        lista_jednog_korisnika = []
        ime, lozinka = line.split(delimiter)[0], line.split(delimiter)[1].strip()

        lista_jednog_korisnika.append(ime)
        lista_jednog_korisnika.append(lozinka)

        lista_korisnika.append(lista_jednog_korisnika)

    return lista_korisnika


def main():
    print(citaj_fajl('korisnici.txt', '|'))



main()