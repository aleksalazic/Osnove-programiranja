
def ispisi_proizvode():
	proizvodi = open('proizvodi.txt', 'r')
	print('{0:>17}{1:>15}{2:>18}'.format('naziv', 'cena', 'kolicina'))
	print(50*'-')
	for i, proizvod in enumerate(proizvodi):
		podaci = proizvod.split('|')
		naziv, cena, kolicina = podaci[0], podaci[1], podaci[2]
		print('{0}.{1:>15}{2:>15}{3:>19}'.format(i+1, naziv, cena, kolicina))
	
	proizvodi.close()



def dodaj_proizvod(naziv, cena, kolicina):
	proizvodi = open('proizvodi.txt', 'a')
	print('{0}|{1}|{2}'.format(naziv, cena, kolicina), file=proizvodi)
	proizvodi.close()

	ispisi_proizvode()
	


def prijava(ime, lozinka):
	prodavci = open('prodavci.txt', 'r')
	for prodavac in prodavci:
		podaci = prodavac.split('|')
		ime_fajl, lozinka_fajl = podaci[0], podaci[1].strip()
		if ime == ime_fajl and lozinka == lozinka_fajl:
			prodavci.close()
			return True

	prodavci.close()	
	return False



def main():

	while True:

		print('Prijavite se na sistem')
		ime = input('Ime prodavca: ')
		lozinka = input('Unesite lozinku: ')

		if prijava(ime, lozinka):
			print('Uspesno ste se ulogovali...')
			while True:
				print('\nPodaci o proizvodu: ')

				naziv = input('Unesite naziv: ')
				if naziv == 'quit':
					break
				
				cena = input('Unesite cenu: ')
				if cena == 'quit':
					break
				
				kolicina = input('Unesite kolicinu: ')
				if kolicina == 'quit':
					break
				
				dodaj_proizvod(naziv, cena, kolicina)

			break
		else:
			print('Pogresno ime ili lozinka, pokusajte ponovo...')
		
		

main()
