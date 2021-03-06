# 4
def adjacentElementsProduct(inputArray):
    mx = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i + 1] > mx:
            mx = inputArray[i] * inputArray[i + 1]
    return mx


# 5
def shapeArea(n):
    area = 1
    for i in range(1, n):
        area += i * 4
    return area


# 6
def makeArrayConsecutive2(statues):
    statues.sort()
    prev = min(statues)
    acc = 0
    for elem in statues[1:]:
        if elem - prev != 1:
            acc += elem - prev - 1
        prev = elem
    return acc

# 7
def almostIncreasingSequence(sequence):
    acc = False
    i = 0
    ran = len(sequence)

    while i < ran:
        curr = sequence[i]

        if i == 0:
            prev = None
        else:
            prev = sequence[i - 1]
        if i >= len(sequence) - 1:
            nxt = None
        else:
            nxt = sequence[i + 1]
        if prev and nxt:
            if not (prev < nxt) and nxt < curr and not acc:
                del sequence[i + 1]
                i -= 1
                ran -= 1
                acc = True
            elif not (prev < nxt) and prev > curr and not acc:
                del sequence[i - 1]
                i -= 1
                ran -= 1
                acc = True
            elif not (prev < curr < nxt) and not acc:
                del sequence[i]
                i -= 1
                ran -= 1
                acc = True
            elif not (prev < curr < nxt) and acc:
                return False
        elif prev:
            if prev >= curr and acc:
                return False
        elif nxt:
            if nxt <= curr and acc:
                return False

        i += 1
    return True


# 8
def matrixElementsSum(matrix):
    topLevel = [len(matrix)] * len(matrix[0])
    total = 0
    for j, elem in enumerate(matrix):
        for i, e in enumerate(elem):
            if e == 0 and topLevel[i] > e:
                topLevel[i] = j
            elif e != 0 and j < topLevel[i]:
                total += e
    # print(topLevel,"\n")
    return total
