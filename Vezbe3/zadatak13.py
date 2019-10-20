import math

def main():
    a, b, c = eval(input('Unesite stranice trougla odvojene zarezom: '))

    s = (a + b + c)/2

    povrsina_trougla = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print('Povrsina trougla: ', povrsina_trougla)


main()