
def sirakuza(x):
    lista = []
    broj = x
    while broj != 1:
        if broj % 2 == 0:
            broj = broj / 2
        else:
            broj = 3 * broj + 1
        lista.append(int(broj))

    return lista


def main():
    print(sirakuza(5))

main()