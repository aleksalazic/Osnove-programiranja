# Zadatak 3. Indeks telesne mase se računa po sledećoj formuli 
# BMI = m/(h*h) u kojoj je m masa u
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





def indeks_telesne_mase(tezina, visina):
    bmi = tezina/(visina**2)
    if bmi < 18.5:
        return 'Pothranjenost'
    elif 18.5 <= bmi < 25:
        return 'Idealna telesna tezina'
    elif 25 <= bmi < 30:
        return 'Preterana telesna tezina'
    else:
        return 'Gojaznost'



def main():
    print(indeks_telesne_mase(55, 1.8))
    print(indeks_telesne_mase(75, 1.8))
    print(indeks_telesne_mase(81, 1.8))
    print(indeks_telesne_mase(120, 1.8))



main()