def is_pangram(s):
    new=""
    wynik=[]
    for i in s:
        new+=i.strip()
    print(new)
    for i in new:
            if  ord(i)>65 and ord(i)<90:
                wynik.append(i)
            elif  ord(i)>97 and ord(i)<122:
                wynik.append(i)
    print(wynik)



print(is_pangram("The quick, brown fox jumps over the lazy dog!"))