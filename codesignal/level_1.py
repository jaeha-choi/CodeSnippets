def add(param1, param2):
    return param1 + param2


def centuryFromYear(year):
    return (year - 1) // 100 + 1


def checkPalindrome(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[-(i + 1)]:
            return False
    return True
