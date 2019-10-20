def main():
    n = int(input('Unesite broj brojeva: '))
    suma = 0
    for i in range(0, n):
        a = float(input('Unesite broj: '))
        suma += a
    prosek = float(suma/n)
    print(prosek)

main()