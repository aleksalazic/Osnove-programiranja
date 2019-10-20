

def main():
    n = int(input('Unesite duzinu fibnacijevog niza: '))
    prvi = 0
    drugi = 1

    for i in range(0, n):
        temp = prvi
        prvi = drugi
        drugi = temp + prvi
    
    print('{0}. u nizu: {1}'.format(n, prvi)) 


main()