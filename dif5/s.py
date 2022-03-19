def power(x, y, n):
    wyn = 1 
    x = x % n    
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y & 1) == 1) :
            wyn = (wyn * x) % n
        y = y >> 1     
        x = (x * x) % n 
    return wyn
     
print(power(2,3,5))