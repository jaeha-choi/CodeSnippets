# 19
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight)


# 20
def arrayMaximalAdjacentDifference(inputArray):
    return max(abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1))


# 21
def isIPv4Address(inputString):
    inp = inputString.split(".")
    if len(inp) != 4:
        return False

    for elem in inp:
        if elem.isdigit():
            iElem = int(elem)
            if not 0 <= iElem <= 255 or str(iElem) != elem:
                return False
        else:
            return False
    return True

# 22
def avoidObstacles(inputArray):
    i = 1
    result = False
    while True:
        li = range(0,max(inputArray)+i,i)
        for val in inputArray:
            if val in li:
                i += 1
                result = False
                break
            result = True
        if result:
            return i


# 23
def boxBlur(image):
    newImage = []
    for r, row in enumerate(image[1:-1]):
        newRow = []
        for c, pixel in enumerate(row[1:-1]):
            val = sum(image[r][c:c+3])
            val += sum(image[r+1][c:c+3])
            val += sum(image[r+2][c:c+3])
            newRow.append(int(val/9))
        newImage.append(newRow)
    return newImage


# 24
def minesweeper(matrix):
    newMatrix = []
    for r, row in enumerate(matrix):
        newRow = []
        for c, elem in enumerate(row):
            count = 0
            if r - 1 < 0:
                ker = [r, r + 1]
            elif r >= len(matrix) - 1:
                ker = [r - 1, r]
            else:
                ker = [r - 1, r + 1]

            if c - 1 < 0:
                co = [c, c + 1]
            elif c >= len(row) - 1:
                co = [c - 1, c]
            else:
                co = [c - 1, c + 1]

            for i in range(ker[0], ker[1] + 1):
                for j in range(co[0], co[1] + 1):
                    if matrix[i][j]:
                        count += 1

            if elem:
                count -= 1
            newRow.append(count)
        newMatrix.append(newRow)
    return newMatrix
