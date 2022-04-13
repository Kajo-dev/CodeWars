def permutations(s):
    from itertools import permutations
    tab=[]
    for i in range(len(s)):
        tab.append(s[i])
    perm=permutations(tab)
    wynik=[]
    for i in list(perm):
        pom=i
        slowo=''
        for k in range(len(pom)):
            slowo+=pom[k]
        wynik.append(slowo)
        wynik=list(set(wynik))
    return wynik
    
print(permutations('aabb'))

