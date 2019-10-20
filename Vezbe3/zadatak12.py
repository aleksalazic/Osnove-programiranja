#Posto pise int aritmetika u zadatku pretpostavljam da vrednosti trebaju biti celobrojne.


def main():
    year = eval(input('Unesite 4-cifrenu godinu: '))
    C = int(year/100)

    epakt = int((8 + C/4 - C + ((8*C + 13)/25) + 11*(year%19))%30)

    print(epakt)

main()