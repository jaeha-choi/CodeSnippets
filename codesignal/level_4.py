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
