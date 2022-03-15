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


class Queue:

    def __init__(self, item=None):
        self.__head = self.__tail = None
        self.__size = 0
        if item is not None:
            self.enqueue(item)

    def __eq__(self, other):
        return self.size() == other.size()

    def __le__(self, other):
        return self.size() <= other.size()

    def __lt__(self, other):
        return self.size() < other.size()

    def __str__(self):
        return "Queue({})".format(self.size())

    def __repr__(self):
        return self.__str__()

    def size(self):
        return self.__size

    def enqueue(self, item):
        new = Node(item)

        if self.__head is None:
            self.__head = self.__tail = new
        else:
            self.__tail.next = new
            self.__tail = new
        self.__size += 1

    def dequeue(self):
        if self.size() == 0:
            raise RuntimeError("Queue is empty")
        item = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return item
