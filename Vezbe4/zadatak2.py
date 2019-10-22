def main():
	reci = input('Unesite reci: ')
	lista = reci.split(' ')
	akronim = ''
	for rec in lista:
		akronim += rec[0].upper()

	print(akronim)


main()