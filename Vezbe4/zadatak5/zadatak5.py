def main():
    korisnici = open('korisnici.txt', 'r')
    racuni = open('racuni.txt', 'r')
    statistika = open('statistika.txt', 'a')


    lista_korisnika = []
    lista_racuna = []

    for korisnik in korisnici:
        ime = korisnik.split('|')[0]
        lista_korisnika.append(ime)

    for i, racun in enumerate(racuni):
        suma = 0
        lista_racuna = racun.split('|')
        for cena in lista_racuna:
            suma += int(cena)

        prosek = float(suma/len(lista_racuna))

        print('{0}|{1}|{2:5.2f}'.format(lista_korisnika[i], suma, prosek), file=statistika)

    korisnici.close()
    racuni.close()
    statistika.close()


main()