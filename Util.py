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
                pass
            else:
                decnum += 1
            roundedvalue += i
        else:
            if i in ["0", "1", "2", "3", "4"]:
                ...
            else:
                roundedvalue = roundedvalue.replace(
                    roundedvalue[len(roundedvalue) - 1],
                    str(int(roundedvalue[len(roundedvalue) - 1]) + 1),
                    -1,
                )
    value = roundedvalue
    return value


def roundliza(value: str):
    if "." in value:
        head, tail = value.split(".")
        if head != "0":
            lenh = len(head)
        else:
            lenh = 0
        for i in range(len(tail)):
            if int(tail[i]):
                return str(round(float(value), i + 3 - lenh))
    return value


def inform(debuglevel: int, normal: str, full: str) -> None:
    if debuglevel == 0:
        pass
    elif debuglevel == 1:
        print(normal)
    else:
        print(full)
