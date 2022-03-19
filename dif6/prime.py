def czypierwsza(liczba):
    liczba=int(liczba)
    if liczba==2:
        return True
    if liczba%2==0 or liczba<=1:
        return False
    pierwiastek =int(liczba**0.5)+1
    for i in range(3,pierwiastek,2):
        if liczba%i==0:
            return False
    return True


from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True

