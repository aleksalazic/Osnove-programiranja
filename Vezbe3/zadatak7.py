
def main():
    atom_C = eval(input('Unesite broj atoma ugljenika: '))
    atom_H = eval(input('Unesite broj atoma vodonika: '))

    mol_masa_molekula = atom_C * 12.011 + atom_H * 1.0079

    print('Molekularna masa jedinjenja: {}'.format(mol_masa_molekula))




main()