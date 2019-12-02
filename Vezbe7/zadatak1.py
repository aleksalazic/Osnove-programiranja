def napravi_tabelu(v_0, v_n, t_0, t_n):
    for i in range(v_0, v_n+2):
        s = ''
        if i >= v_0 + 1:
            s = 'v=' + str(i-1) 
        for j in range(t_0, t_n + 1):
            if i == v_0:
                s += '\tt=' + str(j) + '\t'
            else: 
                vrednosti = 3.74 + 0.6215*j - 35.75*((i-1)**0.16) + 0.4275*j*((i-1)**0.16)
                s += '\t' + str(vrednosti)[0:5] + '\t'

        print(s)

def main():
    napravi_tabelu(0, 10, 5, 10)

main()