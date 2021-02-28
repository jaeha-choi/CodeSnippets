# 34
def extractEachKth(inputArray, k):
    if 0 < k and k < len(inputArray):
        acc = 0
        for i in range(k-1, len(inputArray), k):
            inputArray.remove(inputArray[i-acc])
            acc += 1
    return inputArray

