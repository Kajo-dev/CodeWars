def validate_pin(pin):
    if pin.isnumeric() and (len(pin)==4 or len(pin)==6):
        pom=pin
        pom=float(pom)
        if pom>=0:
            return True
    else:
        return False

print(validate_pin('-12345'))