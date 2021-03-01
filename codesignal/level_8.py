# 34
def extractEachKth(inputArray, k):
    if 0 < k and k < len(inputArray):
        acc = 0
        for i in range(k-1, len(inputArray), k):
            inputArray.remove(inputArray[i-acc])
            acc += 1
    return inputArray


# 35
def firstDigit(inputString):
    for s in inputString:
        if s.isdigit():
            return s


# 36
def differentSymbolsNaive(s):
    se = set()
    for elem in s:
        se.add(elem)
    return len(se)

