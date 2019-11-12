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


def citaj_iz_fajla(fajl, delimiter):
    korisnici_fajl = open(fajl, 'r')
    lista_korisnika = []

    for korisnik in korisnici_fajl:
        k = korisnik.strip().split(delimiter)
        lista_korisnika.append(k)

    korisnici_fajl.close()

    return lista_korisnika


def main():
    print(citaj_iz_fajla('korisnici.txt', '|'))

main()
