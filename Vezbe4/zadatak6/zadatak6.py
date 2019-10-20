import re

def main():
    neformatiran = open('neformatiranTekst.txt', 'r')
    formatiran = open('formatiran.txt', 'a')

    naslov = ''
    paragraf = ''
    
    naslov = neformatiran.readline()
    naslov = re.sub(' +', ' ', naslov).strip()
    naslov_reci = []
    for rec in naslov.split(' '):
        rec = rec.capitalize()
        naslov_reci.append(rec)

    naslov = ' '.join(naslov_reci).strip()
    print('{0:^100s}\n'.format(naslov), file=formatiran)

    

    for line in neformatiran:
        paragraf = line
        paragraf = re.sub(' +', ' ', paragraf).strip()
        paragraf_reci = paragraf.split(' ')
        paragraf_reci[0] = paragraf_reci[0].capitalize()
        for i, rec in enumerate(paragraf_reci):
            
            if i < len(paragraf_reci)-1:
                if (rec.find('?') or rec.find('!')  or rec.find('.') or rec.find('...')) != -1:
                    paragraf_reci[i+1] = paragraf_reci[i+1].capitalize()

        paragraf = ' '.join(paragraf_reci).strip()

        print('     {0}'.format(paragraf), file=formatiran)



    neformatiran.close()
    formatiran.close()





main()