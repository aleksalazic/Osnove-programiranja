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






def citaj_iz_fajla(fajl, delimiter):
    korisnici_fajl = open(fajl, 'r')
    lista_korisnika = []

    for korisnik in korisnici_fajl:
        k = korisnik.strip().split(delimiter)
        lista_korisnika.append(k)

    korisnici_fajl.close()

    return lista_korisnika




def upis_u_fajl(korisnicko_ime, lozinka, ime_fajla, delimiter):

    korisnici_unos = open(ime_fajla, 'a')
    print('{0}{1}{2}'.format(korisnicko_ime, delimiter, lozinka), file=korisnici_unos)

    korisnici_unos.close()

    return citaj_iz_fajla(ime_fajla, delimiter)



def main():

    print(upis_u_fajl('marko', 'markovic', 'korisnici.txt', '|'))
    



main()



