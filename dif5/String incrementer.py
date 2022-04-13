from curses.ascii import isdigit
import string

def increment_string(strng):
    if len(strng)==0:
        return '1'
    else:
        number=1
        for i in range(len(strng)):
            if isdigit(strng[i])==True:
                pom=int(strng[i])
                number+=pom
        if number<10:   
            number=str(number)
            strng=strng[::-1]
            co=strng[0]
            strng=strng.replace(co,number)
            strng=strng[::-1]
            return strng


print(increment_string('foobar0012'))