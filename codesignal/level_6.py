# 25
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i, elem in enumerate(inputArray):
        if elem == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray


# 26
def evenDigitsOnly(n):
    for i in str(n):
        if int(i) % 2 == 1:
            return False
    return True


# 27
import re
def variableName(name):
    return bool(re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", name))


# 28
def alphabeticShift(inputString):
    word = ""
    for ch in inputString:
        ch = ord(ch)
        if ch == ord('z'):
            word += "a"
        else:
            word += str(chr(ch+1))
    return word


# 29
def chessBoardCellColor(cell1, cell2):
    di = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    return (di[cell1[0]]+int(cell1[1])) % 2 == (di[cell2[0]]+int(cell2[1])) % 2
