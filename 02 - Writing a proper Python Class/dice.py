import random


class Dice(object):
    """
    Multi-sided dice

    Instance Variables:
        int sides
        int value
    """

    def __init__(self, sides):
        self.sides = sides
        self.value = 0
        self.roll()

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Dice({}) : {}".format(self.sides, self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def roll(self):
        self.value = random.randrange(1, self.sides + 1)


def main():
    d6 = Dice(5)
    for i in range(5):
        print(d6)
        d6.roll()

    d_list = [Dice(6), Dice(20)]
    print(d_list)


main()
