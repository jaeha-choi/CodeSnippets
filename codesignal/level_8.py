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


# 37
def arrayMaxConsecutiveSum(inputArray, k):
    mx = inputArray[0]
    curr = sum(inputArray[:k])
    prev_elem = inputArray[0]
    for i in range(1, len(inputArray)-k+1):
        # print(i, inputArray[i], k)
        if mx < curr:
            mx = curr
        curr -= prev_elem
        prev_elem = inputArray[i]
        curr += inputArray[i+k-1]
    if mx < curr:
        mx = curr
    return mx
