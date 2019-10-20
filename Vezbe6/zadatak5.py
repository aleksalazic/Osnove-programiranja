# Zadatak 5. Dadilja naplaćuje 150din po satu čuvanja dece do 9 sati uveče, a 100din po satu čuvanja dece
# posle 9 sati uveče. Napiši funkciju koja kao parametre prima vreme kada dadilja počinje da čuva deci i
# kada završava učuvanje dece, a vraća poruku o zaradi koja treba se isplati. Vreme je zadato u formatu
# hh:mm, a predpostavlja se da se čuvanje dece odvija u periodu od 24h.
# Primer izvršavanja programa:
# >>> print(dadilja('18:35','22:50'))
# zarada dadilje je 546din


def konvertuj_vreme(vreme):
    vreme_niz = vreme.split(':')
    konvertovano_vreme = int(vreme_niz[0]) + int(vreme_niz[1])/60

    return konvertovano_vreme



def dadilja(pocetak, kraj):
    
    vreme_pocetak = konvertuj_vreme(pocetak)
    vreme_kraj = konvertuj_vreme(kraj)

    if vreme_pocetak <= 21 and vreme_kraj <= 21 and vreme_kraj > vreme_pocetak:
        return 150 * (vreme_kraj - vreme_pocetak)

    elif vreme_pocetak <= 21 and vreme_kraj > 21:
        zarada_po_150 = (21 - vreme_pocetak) * 150
        zarada_po_100 = (vreme_kraj - 21) * 100

        return int(zarada_po_150 + zarada_po_100) + 1 

    elif vreme_pocetak <= 21 and vreme_kraj < 21 and vreme_pocetak > vreme_kraj:
        zarada_po_150 = (21 - vreme_pocetak) * 150
        zarada_po_100 = (24 - 21 + vreme_kraj) * 100
        
        return int(zarada_po_150 + zarada_po_100) + 1
       
        
        

def main():
    print(dadilja('18:35', '22:50'))
    #print(dadilja('20:00', '02:00'))



main()