# Zadatak 3. Indeks telesne mase se računa po sledećoj formuli 2
# h
# m
# BMI = u kojoj je m masa u
# kilogramima, a h visina u metrima. U tabeli je data preporučena klasifikacija indeksa telesne mase:

# BMI Klasifikacija
# <18,5 Pothranjenost
# 18,5 - 25 Idealna telesna težina
# 25 - 30 Preterana telesna težina
# >30 Gojaznost

# Napiši funkciju koja prima težinu u kilogramima i visinu, a vraća kategoriju iz klasifikacije BMI.
# Primer izvršavanja programa:
# >>> print(indeksTelesneMase(55,1.8))
# 'pothranjenost'
# >>> print(indeksTelesneMase(75,1.8))
# 'idealna telesna tezina'
# >>> print(indeksTelesneMase(81,1.8))
# 'preterana telesna tezina'
# >>> print(indeksTelesneMase(120,1.8))
# 'gojaznost'


def kazna(brzina, ogranicenje):
    if brzina > ogranicenje and brzina < 120:
        kazna = 5000 + (brzina - ogranicenje) * 500
        return 'Vasa kazna iznosi {0} din'.format(kazna)
    elif brzina > 120:
        kazna = 5000 + (brzina - ogranicenje) * 500 + 10000
        return 'Vasa kazna iznosi {0} din'.format(kazna)
    else:
        return 'Niste prekoracili brzinu'
    


def main():
    print(kazna(80, 60))
    print(kazna(50, 60))
    print(kazna(130, 60))

main()