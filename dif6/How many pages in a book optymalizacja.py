def amount_of_pages(summary):
    wynik=0
    for i in range(1,summary+1):
        while wynik<summary:
            i=str(i)
            if len(i)==1:
                wynik+=1
            elif len(i)==2:
                wynik+=2
            elif len(i)==3:
                wynik+=3
            elif len(i)==4:
                wynik+=4
            elif len(i)==5:
                wynik+=5
            elif len(i)==6:
                wynik+=6
            i=int(i)
            w=i
            break
    return w

print(amount_of_pages(100000))