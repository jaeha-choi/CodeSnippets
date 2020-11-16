def allLongestStrings(inputArray):
    li = []

    for elem in inputArray:
        li.append(len(elem))
    mx = max(li)

    ret = []
    for i, elem in enumerate(li):
        if elem == mx:
            ret.append(inputArray[i])

    return ret


def commonCharacterCount(s1, s2):
    d1 = {}
    d2 = {}
    for ch in s1:
        d1.setdefault(ch, 0)
        d1[ch] += 1

    for ch in s2:
        d2.setdefault(ch, 0)
        d2[ch] += 1

    cnt = 0
    for key, value in d1.items():
        if key in d2:
            cnt += min(d2[key], value)
            # print(key, d2[key], value , "\n")
    return cnt
