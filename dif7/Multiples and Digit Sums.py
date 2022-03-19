def procedure(i):
    liczba=i
    wyniki=[]
    dodawania=[]
    wyniki.append(liczba)
    while liczba<100:
        liczba+=i
        wyniki.append(liczba)
    for k in range(len(wyniki)):
        zamiana=str(wyniki[k])
        do_dodania=[]
        for l in range(len(zamiana)):
            do_dodania.append(zamiana[l])
        
        for h in range(len(do_dodania)):
            dodatnia=do_dodania[h]
            dodatnia=+int(do_dodania[h])
        dodawania.append(dodatnia)
        print(dodawania)
    return wyniki

print(procedure(25))