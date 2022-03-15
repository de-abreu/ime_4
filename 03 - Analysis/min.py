import time
from random import randrange


def min(numbers, length):
    min = numbers[0]

    for i in range(1, length):
        if numbers[i] < min:
            min = numbers[i]
    return min


def dumbMin(numbers, length):
    j = 0

    for i in range(length - 1):
        for j in range(i + 1, length):
            if (numbers[j] < numbers[i]):
                break
            if (j == length - 1):
                return numbers[i]
    return numbers[j]


def main():
    print("This program tests two distinct functions to find the minimum value contained within a list. Such list is geneerated with randm values between 0 and a billion.")
    length = int(input("Type in a length for the list of values: "))
    numbers = [randrange(0, length) for x in range(length)]

    print("\nEvaluating function min...")
    start = time.time()
    print("Minimum is", min(numbers, length))
    print("Runtime:", time.time() - start, "seconds.")

    print("\nEvaluating function DumbMin...")
    start = time.time()
    print("Minimum is", dumbMin(numbers, length))
    print("Runtime:", time.time() - start, "seconds.")


main()
