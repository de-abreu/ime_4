class Node:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    data = property(get_data, set_data)

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    next = property(get_next, set_next)

    def __str__(self):
        return str(self.__data)


class Stack:
    def __init__(self, item=None):
        self.__top = None
        self.__size = 0
        if item is not None:
            self.push(item)

    def __get_size(self):
        return self.__size

    def __set_size(self, value):
        self.__size = int(value)

    size = property(__get_size, __set_size)

    def isEmpty(self):
        return True if self.__top is None else False

    def push(self, item):
        new = Node(item)
        new.next = self.__top
        self.__top = new
        self.size = self.size + 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        data = self.__top.data
        self.__top = self.__top.next
        self.size = self.size - 1
        return data

    def peek(self, size=1):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        if not isinstance(size, int) or size < 1:
            raise ValueError("Only positive integers are accepted.")

        current = self.__top
        dataset = []
        while current is not None and size > 0:
            dataset.append(current.data)
            current = current.next
            size -= 1
        return dataset

    def __str__(self):
        return "Stack({}): {}".format(self.size, self.__repr__())

    def __repr__(self):
        return str(self.peek(self.size))

    def __eq__(self, other):
        return self.size == other.size

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __add__(self, other):
        result = Stack()
        for item in self.peek(self.size) + other.peek(other.size):
            result.push(item)
        return result

    def __mul__(self, multiplier):
        result = Stack()
        for item in self.peek(self.size) * multiplier:
            result.push(item)
        return result
