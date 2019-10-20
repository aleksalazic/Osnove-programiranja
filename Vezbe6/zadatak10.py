def prestupna_godina(godina):
    if godina % 4 == 0 and godina % 100 != 0:
        return True
    elif godina % 400 == 0:
        return True
    else:
        return False


def redni_br_dana(datum):
    dan = int(datum.split('/')[0])
    mesec = int(datum.split('/')[1])
    godina = int(datum.split('/')[2])

    
    if mesec <= 2:
        dan_u_godini = 31*(mesec - 1) + dan
    elif mesec > 2:
        if not prestupna_godina(godina):
            dan_u_godini = 31*(mesec -1 ) + dan - int((4*mesec + 23)/10)
        else:
            dan_u_godini = 31*(mesec -1 ) + dan - int((4*mesec + 23)/10) + 1

    return dan_u_godini


def main():
    print(redni_br_dana('5/3/2020'))

main()