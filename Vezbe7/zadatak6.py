
def nzd(m, n):
	while m != 0:
		m, n = n%m, m
	
	return n
	


def main():

	print(nzd(25,15))

main()
