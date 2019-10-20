def main():
    n = eval(input('Unesite broj brojeva: '))
    
    suma = 0

    for i in range(n):
        broj = float(input('Unesite broj: '))
        suma += broj

    print(suma)

main()