from random import randrange


class quickList(list):
    """ A class to extend the methods available for list variables. """

    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def swap(self, a, b):
        """ Swap the values at the list indexes a and b"""

        tmp = self.values[a]
        self.values[a] = self.values[b]
        self.values[b] = tmp

    def smallest(self, n=0):
        """
        Find the nth smallest value in the list (counting from 0).

        This method is based on the Quick Select algorithm:
        https://en.wikipedia.org/wiki/Quickselect

        Parameters
        ----------

        n: int
            The index of the value, where the list sorted by value.

        Returns
        -------

        int
            The index of the ith smallest value.
        """

        def partition(self, pivot, left, right):
            i = j = left

            self.swap(pivot, right)
            while (i < right):
                if self.values[i] <= self.values[right]:
                    self.swap(i, j)
                    j += 1
                i += 1
            self.swap(i, j)
            return j

        right = len(self.values) - 1
        left = 0
        pivot = -1

        if n > right:
            n = right
        while pivot != n:
            pivot = partition(self, n, left, right)
            if n < pivot:
                right = pivot - 1
            elif n > pivot:
                left = pivot + 1
        return n


def main():
    print("This program finds the nth smallest value in a list of random numbers.")
    size = int(input("Type in the size of the list: "))
    n = int(input("Type in a value for n: "))
    if size < 1 or n < 1:
        print("Not a valid (positive) integer value.")
        return
    numbers = quickList([randrange(0, size) for i in range(size)])
    print("List of values:", numbers)
    print("Nth smallest value:", numbers.smallest(n - 1))


main()
