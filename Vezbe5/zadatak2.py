# Zadatak 2. Napiši program koji za zadati niz brojeva:
# • Ispisuje najmanji element niza
# • Ispisuje najveći element niza
# • Ispisuje sumu vrednosti u nizu
# • Ispisuje srednju vrednost za niz
# Svaki od zadatih zahteva trebada bude implementiran kao posebna funkcija.
# Primer izvršavanja programa:
# >>> karakteristikeNiza([1,2,3,4,5,-1,6])
# najmanji element niza je: -1
# najveci element niza je: 6
# suma elemenata niza je: 20
# prosek elemenata niza je: 2.857142857142857


def najmanji_element_niza(niz):
    min = niz[0]
    for i in range(1, len(niz)):
        if min > niz[i]:
            min = niz[i]

    return min


def najveci_element_niza(niz):
    max = niz[0]
    for i in range(1, len(niz)):
        if max < niz[i]:
            max = niz[i]
    
    return max


def suma_niza(niz):
    suma = 0
    for i in range(len(niz)):
        suma += niz[i]

    return suma


def prosek_niza(niz):
    return float(suma_niza(niz)/len(niz))




def karakteristikeNiza(niz):
    print('Najmanji element niza je: ', najmanji_element_niza(niz))
    print('Najveci element niza je: ', najveci_element_niza(niz))
    print('Suma elemenata niza je: ', suma_niza(niz))
    print('Prosek elemenata niza je: ', prosek_niza(niz))




def main():
    karakteristikeNiza([1, 2, 3, 4, 5, -1, 6])


main()