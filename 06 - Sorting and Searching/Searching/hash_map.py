import math


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __repr__(self):
        return str((self.key, self.data))

    def __str__(self):
        return "-Node {}".format(self.__repr__())


class Primes:
    """
    A list to calculate and store all prime numbers that are less or equal to n
    """

    def __init__(self):
        self.__list = [2, 3]

    def __getitem__(self, index):
        return self.__list[index]

    def __len__(self):
        return len(self.__list)

    def __append(self, i):
        self.__list.append(i)

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current < len(self):
            self.__current += 1
            return self[self.__current - 1]
        raise StopIteration

    def __isPrime(self, i):
        if i < 2:
            return False
        for p in self:
            if i % p == 0:
                return False
        return True

    def __update_list(self, max):
        i = self[-1] + 2
        while self[-1] < max:
            if self.__isPrime(i):
                self.__append(i)
            i += 2

    def __contains__(self, n):
        root = math.ceil(n**(1/2))
        self.__update_list(root)
        return n in self.__list or self.__isPrime(n)


class Map:
    def __init__(self, key=None, data=None):
        self.__slots = [None]
        self.__entries = 0
        self.__primes = Primes()
        if not (key is None and data is None):
            self[key] = data

    def __len__(self):
        return self.__entries

    def __eq__(self, other):
        return len(self) == len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __hash(self, key, size):
        index = 0
        weight = 1
        for c in str(key):
            index += ord(c) * weight
            weight += 1
        return index % size

    def __rehash(self, index, size):
        return (index + size // 4 + 1) % size

    def __find_index(self, key):
        index = self.__hash(key, len(self.__slots))

        while self.__slots[index] and self.__slots[index].key != key:
            index = self.__rehash(index, len(self.__slots))
        return index

    def __nextPrime(self, n):
        while n not in self.__primes:
            n += 1
        return n

    def __grow(self):
        size = self.__nextPrime(2 * len(self.__slots))
        new_slots = [None] * size

        for node in self.__slots:
            index = self.__hash(node.key, len(new_slots))
            while new_slots[index]:
                index = self.__rehash(index, len(new_slots))
            new_slots[index] = node
        self.__slots = new_slots

    def __setitem__(self, key, data):
        index = self.__find_index(key)

        if self.__slots[index] is None:
            self.__slots[index] = Node(key, data)
            self.__entries += 1
            if len(self.__slots) == len(self):
                self.__grow()
        else:
            self.__slots[index].data = data

    def __getitem__(self, key):
        index = self.__find_index(key)

        if self.__slots[index] is None:
            return None
        return self.__slots[index].data

    def __contains__(self, key):
        index = self.__find_index(key)

        return self.__slots[index] is not None

    def __delitem__(self, key):
        index = self.__find_index(key)

        if not self.__slots[index]:
            raise KeyError("Key not found")
        self.__slots[index] = None
        self.__entries -= 1

    def __iter__(self):
        for i in range(len(self.__slots)):
            if self.__slots[i]:
                yield self.__slots[i]

    def __repr__(self):
        return str([x for x in self])

    def __str__(self):
        return "Map (size {}): {}".format(len(self), self.__repr__())
