# Zadatak 1. Napiši funkciju koji obračunava zaradu radnika. Radnici koji rade više od 40 sati nedeljno su
# plaćeni 1.5 puta više nego što bi bili plaćeni da rade do 40 sati nedeljno. Broj radnih sati po danima
# završene radne nedelje se učitava iz fajla. Funkcija kao parametar prima putanju do fajla sa radnim
# satima i cenu radnog sata i ispisuje imena i zarade radnika.
# Primer izvrašavanja programa:
# Za fajl radnici.txt
# pera|8|9|7|8|9
# jova|8|8|7|8|7
# steva|8|8|9|8|7
# rezultat poziva funkcije treba da bude:
# >>> racunanjeZarade("radnici.txt",1000)
# ime: pera
# zarada: 61500.0
# ime: jova
# zarada: 38000
# ime: steva
# zarada: 40000




def zarada_po_satu(sati, cena_sata):
    if sati > 40:
        zarada = sati * cena_sata * 1.5
    else:
        zarada = sati * cena_sata
    
    return zarada


def racunanje_zarade(ime_fajla, cena_sata):
    radnici = open(ime_fajla, 'r')
    
    for line in radnici:
        suma_sati = 0
        radnik = []
        radnik = line.split('|')
        ime_radnika = radnik[0]

        for i, sati in enumerate(radnik):
            if i != 0:
                suma_sati += int(sati)
        
        
        print('Ime: {0}\nZarada: {1}'.format(ime_radnika, zarada_po_satu(suma_sati, cena_sata)))
        
            





def main():
    racunanje_zarade('radnici.txt', 1000)

main()