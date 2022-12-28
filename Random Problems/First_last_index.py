arr = [2,4,5,5,5,5,7,9,9]
target = 5

def szukaj(arr,targ):
    start = 0
    end = 0
    for i,v in enumerate(arr):
        if v == targ:
            if start == 0:
                start = i
        else:
            if targ == arr[i - 1]:
                end = i - 1
                break

    wynik = []
    wynik.append(start)
    wynik.append(end)
    
    return wynik
    

print(szukaj(arr,target))
