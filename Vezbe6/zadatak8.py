# Zadatak 8. Godina je prestupna ako je deljiva sa 4, osim ako je posedlja godina u veku, a tada je
# prestupna ako je deljiva sa 400 (na primer 1800 i 1900 nisu prestupne dok 1600 i 2000 jesu). Napisati
# funkciju koji proverava da li je godina prestupna.
# Primer izvršavanja programa:
# >>> print(prestupnaGodina(1983))
# nije prestupna
# >>> print(prestupnaGodina(1984))
# prestupna
# >>> print(prestupnaGodina(1900))
# nije prestupna
# >>> print(prestupnaGodina(2000))
# prestupna



def prestupna_godina(godina):

    if godina % 4 == 0 and godina % 100 != 0:
        return 'Prestupna'
    elif godina % 400 == 0:
        return 'Prestupna'
    else:
        return 'Nije prestupna' 



def main():
    print(prestupna_godina(1983))
    print(prestupna_godina(1984))
    print(prestupna_godina(1900))
    print(prestupna_godina(2000))

main()