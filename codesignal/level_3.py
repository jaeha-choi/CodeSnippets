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


def isLucky(n):
    return sum([int(s) for s in str(n)[:len(str(n)) // 2]]) == sum([int(s) for s in str(n)[len(str(n)) // 2:]])


def sortByHeight(a):
    b = []
    for elem in a:
        if elem != -1:
            b.append(elem)
    b.sort()
    i = 0
    for j, elem in enumerate(a):
        if elem != -1:
            a[j] = b[i]
            i += 1
    return a


def reverseInParentheses(inputString):
    li = []
    parenO = []

    i = 0
    ran = len(inputString)
    while i < ran:
        ch = inputString[i]
        if ch == "(":
            parenO.append(i)
        elif ch == ")":
            start = parenO.pop()
            # "." isnt necessary if you update parentheses' index.
            inputString = inputString[:start] + "." + inputString[i - 1:start:-1] + "." + inputString[i + 1:]
            print(inputString)
            i -= 1
        i += 1
    inputString = inputString.replace(".", "")
    return inputString
