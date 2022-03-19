def permutations(s):
    from itertools import permutations
    perm=permutations(s)
    wynik=[]
    for i in list(perm):
        pom=i
        slowo=''
        for k in range(len(pom)):
            slowo+=pom[k]
        wynik.append(slowo)
    return(list(set(wynik[::-1])))


print(permutations('aabb'))