import math

def prost_broj(broj):
	x = int(math.sqrt(broj))
	for i in range(2, x+1):
		if broj%i == 0:
			return False
			
	return True


def svi_prosti_brojevi(n):
	lista_brojeva = []
	
	for i in range(n):
		if prost_broj(i):
			lista_brojeva.append(i)
			
	return lista_brojeva



def main():

	broj = int(input('Unesite broj: '))
	print(svi_prosti_brojevi(broj))


main()
