def alternatingSums(a):
    b = [0, 0]
    for i, elem in enumerate(a):
        if i % 2 == 0:
            b[0] += elem
        else:
            b[1] += elem
    return b

    # return [sum(a[::2]), sum(a[1::2])]


def addBorder(picture):
    top = "*" * (len(picture[0]) + 2)
    ret = [top]
    for elem in picture:
        ret.append("*" + elem + "*")
    ret.append(top)
    return ret


def areSimilar(a, b):
    if a == b:
        return True
    elif sorted(a) != sorted(b):
        return False
    else:
        temp1 = 0
        count = 0
        for elem1, elem2 in zip(a, b):
            if elem1 != elem2 and count == 0:
                temp1 = elem1
                print(temp1)
                count += 1
            elif elem1 != elem2 and count == 1:
                if temp1 != elem2:
                    return False
    return True
