# Zadatak 4. Napiši funkciju za registrovanje korisnika. Funkcija prima korisničko ime, lozinku, naziv fajla u
# koji se snima i delimiter kojim će biti razdvojeno korisničko ime i lozinka. Korisničko ime i lozinku se
# snimaju u fajl sa zadatim nazivom. Ta funkcija vraća korisnička imena i lozinke svih registrovanih
# korisnika, kao što je specificirano u zadatku 3.
# Primer izvršavanja programa:
# Za fajl korisnici.txt
# pera|peric
# jova|jovic
# steva|stevic
# rezultat poziva funkcije treba da bude:
# >>> print(upisUFajl("marko","markovic","korisnici.txt","|"))
# [['pera', 'peric'], ['jova', 'jovic'], ['steva', 'stevic'], ['marko',
# 'markovic']]
# fajl korisnici.txt nakon navedenog izvršavanja programa treba da sadrži:
# pera|peric
# jova|jovic
# steva|stevic
# marko|markovic





def ispis(fajl, delimiter):
    lista_korisnika = []

    for line in fajl:
        lista_jednog_korisnika = []
        ime_korisnika, lozinka_korisnika = line.split(delimiter)[0], line.split(delimiter)[1].strip()
        lista_jednog_korisnika.append(ime_korisnika)
        lista_jednog_korisnika.append(lozinka_korisnika)

        lista_korisnika.append(lista_jednog_korisnika)

    return lista_korisnika



def upis_u_fajl(korisnicko_ime, lozinka, ime_fajla, delimiter):

    korisnici_unos = open(ime_fajla, 'a')
    print('{0}{1}{2}'.format(korisnicko_ime, delimiter, lozinka), file=korisnici_unos)

    korisnici_unos.close()

    korisnici_ispis = open(ime_fajla, 'r')
    print(ispis(korisnici_ispis, delimiter))

    korisnici_ispis.close()



def main():

    upis_u_fajl('marko', 'markovic', 'korisnici.txt', '|')
    upis_u_fajl('pera', 'peric', 'korisnici.txt', '|')
    upis_u_fajl('steva', 'stevic', 'korisnici.txt', '|')



main()



