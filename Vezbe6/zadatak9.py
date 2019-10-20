# Zadatak 9. Napiši funkciju koji datum prima u obliku dd/mm/gggg i proverava da li je datum validan. Na
# primer 24/5/1962 je validan datu, ali 31/9/2000 nije jer septembar nema 31 dan. Takođe voditi računa i
# o tome da li je godina prestupna.


def prestupna_god(godina):
    if godina % 4 == 0 and godina % 100 != 0:
        return True
    elif godina % 400 == 0:
        return True
    else:
        return False



def datum_validacija(datum):

    dan = int(datum.split('/')[0])
    mesec = int(datum.split('/')[1])
    godina = int(datum.split('/')[2])

    
    if mesec in [1, 3, 5, 7, 8, 10, 12]:
        if 0 < dan <= 31:
            print('Validan')
        else:
            print('Nije validan')
    if mesec in [2, 4, 6, 9, 11]:
        if mesec != 2:
            if 0 < dan <= 30:
                print('Validan')
            else:
                print('Nije validan')
        else:
            if not prestupna_god(godina):
                if 0 < dan <= 28:
                    print('Validan')
                else:
                    print('Nije validan')
            else:
                if 0 < dan <= 29:
                    print('Validan')
                else:
                    print('Nije validan')
        


def main():

    datum_validacija('24/5/1962')

    datum_validacija('31/9/2000')
    


main()