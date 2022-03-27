#'is2 Thi1s T4est 3a'


def order(sentence):
    if len(sentence)<=1:
        return sentence
    else:
        lista=sentence.split(' ')
        kolejnosc=[]
        wynik=[]
        for slowa in lista:
            for i in range(len(slowa)):
                if slowa[i].isdigit():
                    pom=int(slowa[i])
                    kolejnosc.append(pom)
        for i in range(len(lista)):
            mi=min(kolejnosc)
            ind=kolejnosc.index(mi)
            kolejnosc[ind]=10 #nie ma więcej jak 10 
            wynik.append(lista[ind])
        tekst=""
        for i in range(len(wynik)):
            pom=wynik[i]
            tekst+=pom+" "
        tekst=tekst.rstrip(" ")
    return tekst



print(order("4of Fo1r pe6ople g3ood th5e the2"))




