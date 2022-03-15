def cumulativeFrequency(values, exp):
    frequency = [0] * 11

    for i in range(len(values)):
        radix = values[i] // exp % 10
        frequency[radix + 1] += 1
    for i in range(1, 11):
        frequency[i] += frequency[i - 1]
    return frequency


def countingSort(values, exp):
    count = cumulativeFrequency(values, exp)
    sorted = [None] * len(values)

    for i in range(len(values)):
        radix = values[i] // exp % 10
        sorted[count[radix]] = values[i]
        count[radix] += 1
    return sorted


def radixSort(values, max=None):
    exp = 1
    if max is None:
        max = max(values)

    while max // exp > 0:
        values = countingSort(values, exp)
        exp *= 10
    return values
