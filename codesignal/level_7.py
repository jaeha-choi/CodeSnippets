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
# Very similar to Hamiltonian path questions
def visit(curr, d, done):
    mx = len(done)
    for elem in d[curr]:
        if elem not in done:
            done.append(elem)
            curr_mx = visit(elem, d, done)
            done.remove(elem)
            if mx < curr_mx:
                mx = curr_mx
    return mx


def stringsRearrangement(inputArray):
    d = {}
    for idx in range(len(inputArray)):
        d[idx] = []
        for jdx in range(len(inputArray)):
            if idx != jdx:
                count = 0
                for i, j in zip(inputArray[idx], inputArray[jdx]):
                    if i != j:
                        count += 1
                if count == 1:
                    d[idx].append(jdx)
    lengths = [len(val) for val in d.values()]
    start_val = list(d.keys()).index(lengths.index(min(lengths)))

    return visit(start_val, d, [start_val]) == len(inputArray)
