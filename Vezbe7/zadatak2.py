
def broj_godina(kamatna_stopa):
    novac = 1
    glavnica = novac
    i = 0

    while(glavnica < 2 * novac):
        glavnica = glavnica + glavnica*kamatna_stopa
        i += 1

    return i

def main():
    print(broj_godina(0.04))

main()