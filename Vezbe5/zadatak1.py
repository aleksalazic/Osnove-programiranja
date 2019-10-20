# Zadatak 1. Kvadratna jednačina zadata je formatom a*x^2 + b*x + c = 0
# Koreni kvadratne jednačine računaju se kao:
# x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
# x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)    

# Napisati funkciju koja prima parameter a,b i c i vraća rešenja
# kvadratne jednačine. Pri tome se predpostavlja da postoje realni koreni kvadratne jednačine.
# Primer izvršavanja programa:
# >>> print(kvJednacina(-1,5,5))
# (-0.8541019662496847, 5.854101966249685)






import math

def kvJednacina(a, b, c):
    
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    return x1, x2



def main():
    a = eval(input('Unesite parametar A: '))
    b = eval(input('Unesite parametar B: '))
    c = eval(input('Unesite parametar C: '))

    print(kvJednacina(a, b, c))



main()