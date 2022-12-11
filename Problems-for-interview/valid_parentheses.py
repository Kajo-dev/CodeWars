def is_valid(com):
    diff = 0
    for par in com:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return True if diff == 0 else False


print(is_valid(')))((('))