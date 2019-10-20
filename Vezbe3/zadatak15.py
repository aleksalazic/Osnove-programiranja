def main():
    n = eval(input('Unesite broj brojeva: '))
    s = 0

    for i in range(1, n + 1):
        s += i

    print('Rezultat: ', s)

main()