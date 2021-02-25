# 30
def circleOfNumbers(n, firstNumber):
    if firstNumber >= (n / 2):
        return (firstNumber + n/2) - n
    else:
        return firstNumber + n/2


# 31
def depositProfit(deposit, rate, threshold):
    i = 0
    while deposit < threshold:
        deposit += deposit*rate/100
        i += 1
    return i


# 32
def absoluteValuesSumMinimization(a):
    sm = sum(a)
    mnVal = sm
    init = True
    prev = a[0]
    for i in a:
        local_sum = 0
        for elem in a:
            local_sum += abs(elem - i)
        if mnVal > local_sum or init:
            mnVal = local_sum
            prev = i
            init = False
        if mnVal < local_sum:
            return prev
    return prev


# 33
