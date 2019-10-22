import re
import textwrap

def main():
    neformatiran = open('neformatiranTekst.txt', 'r')
    formatiran = open('formatiran.txt', 'a')

    naslov = neformatiran.readline()
    naslov = re.sub(' +', ' ', naslov).strip().title().center(100)
    
    print('{}\n'.format(naslov), file=formatiran)

    
    #Ovo dole verovatno moze more pythonic da se uradi, 
    #ali nije mi python primaran jezik pa ne zamerite

    for paragraf in neformatiran:
        recenice_sa_tackama = []
        recenice_sa_upitnikom = []
        paragraf = re.sub(' +', ' ', paragraf)
        
        
        for recenica_sa_tackom in paragraf.split('.'):
            recenica_sa_tackom = recenica_sa_tackom.strip().capitalize()
            if recenica_sa_tackom.find('?') != -1:
                
                for recenica_sa_upitnikom in recenica_sa_tackom.split('?'):
                    recenica_sa_upitnikom = recenica_sa_upitnikom.strip().capitalize()
                    recenice_sa_upitnikom.append(recenica_sa_upitnikom)

                recenica_sa_tackom = '? '.join(recenice_sa_upitnikom)

            recenice_sa_tackama.append(recenica_sa_tackom)
        
        paragraf = '. '.join(recenice_sa_tackama)
        paragraf = textwrap.fill(paragraf, initial_indent='     ')

        print(paragraf, file=formatiran)


    



    neformatiran.close()
    formatiran.close()





main()