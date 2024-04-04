def roundstr(value: str) -> str:
    decnum = 0
    decbool = False
    roundedvalue = str()
    for i in value:
        if i != "." and decbool == False:
            roundedvalue += i
            continue
        elif decbool == False:
            roundedvalue += i
            decbool = True
            continue
        if decnum < 3:
            if i == "0" and decnum == 0:
                ...
            else:
                decnum += 1
            roundedvalue += i
    value = roundedvalue
    return value
