import math

def prost_broj(broj):
	x = int(math.sqrt(broj))
	for i in range(2, x+1):
		if broj%i == 0:
			return False
			
	return True


def main():
	
	broj = int(input('Unesite broj: '))
	print(prost_broj(broj))


main()
