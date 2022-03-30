def amount_of_pages(summary):
    tab=[]
    wynik=0
    for i in range(1,summary+1):
        tab.append(i)
    for i in tab:
        while wynik<summary:
            i=str(i)
            if len(i)==1:
                wynik+=1
            if len(i)==2:
                wynik+=2
            if len(i)==3:
                wynik+=3
            if len(i)==4:
                wynik+=4
            if len(i)==5:
                wynik+=5
            if len(i)==6:
                wynik+=6
            i=int(i)
            w=i
            break
    return w

print(amount_of_pages(1095))

