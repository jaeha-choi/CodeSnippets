# 14
def alternatingSums(a):
    b = [0, 0]
    for i, elem in enumerate(a):
        if i % 2 == 0:
            b[0] += elem
        else:
            b[1] += elem
    return b

    # return [sum(a[::2]), sum(a[1::2])]


# 15
def addBorder(picture):
    top = "*" * (len(picture[0]) + 2)
    ret = [top]
    for elem in picture:
        ret.append("*" + elem + "*")
    ret.append(top)
    return ret


# 16
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


# 17
def arrayChange(inputArray):
    # Incomplete
    # This also assumes that we can decrement the value instead of increasing
    # acc = 0
    # for i, elem in enumerate(inputArray[1:-1]):
    #     prev = inputArray[i]
    #     curr = inputArray[i+1]
    #     nxt = inputArray[i+2]
    #     if prev >= curr and curr <= nxt:
    #         lowerTo = curr-1

    #         acc += prev - lowerTo
    #         inputArray[i] = lowerTo
    #     elif prev <= curr and curr >= nxt:
    #         if prev+1 < nxt:
    #             lowerTo = nxt-1
    #         else:
    #             lowerTo = prev+1

    #         acc += curr - lowerTo
    #         inputArray[i+1] = lowerTo
    #     print(prev, curr, nxt, "\n")
    # print(inputArray)
    # return acc

    acc = 0
    for i, elem in enumerate(inputArray[1:]):
        prev = inputArray[i]
        curr = inputArray[i + 1]
        if prev >= curr:
            acc += (prev + 1) - curr
            inputArray[i + 1] = prev + 1

    return acc


# 18
def palindromeRearranging(inputString):
    di = {}
    for ch in inputString:
        di.setdefault(ch, 0)
        di[ch] += 1

    flag = False
    for value in di.values():
        if value % 2 == 1:
            if flag:
                return False
            flag = True

    return True
