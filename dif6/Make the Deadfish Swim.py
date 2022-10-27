def parse(data):
    tab = []
    num = 0
    for char in data:
        if char == 'i':
            num+=1
        elif char == 'd':
            num-=1
        elif char == 's':
            num = num * num
        elif char == 'o':
            tab.append(num)
    return tab

