datoteka = open('podaci.txt', 'r')

for line in datoteka:
    podatak = line.split('|')
    print('korisnicko ime: {0}\nlozinka: {1}'.format(podatak[0], podatak[1]))

datoteka.close()