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


class List:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def __eq__(self, other):
        return self.size() == other.size()

    def __le__(self, other):
        return self.size() <= other.size()

    def __lt__(self, other):
        return self.size() < other.size()

    def __add__(self, other):
        result = List()
        for l in self, other:
            current = l.__head
            while current is not None:
                result.add(current.data)
                current = current.next
        return result

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise ValueError("Multiplier is not an integer value.")
        result = List()
        while multiplier > 0:
            result += self
            multiplier -= 1
        return result

    def __repr__(self):
        items = []
        current = self.__head

        while current is not None:
            items.append(current.data)
            current = current.next
        return str(items)

    def __get_head(self):
        return self.__head

    def __set_head(self, node):
        if not isinstance(node, Node):
            raise TypeError(node, "is not a Node object.")
        self.__head = node

    head = property(__get_head, __set_head)

    def __get_size(self):
        return self.__size

    def __set_size(self, value):
        self.__size = int(value)

    size = property(__get_size, __set_size)

    def isEmpty(self):
        return self.__head is None

    def index(self, item):
        current = self.__head
        index = 0

        while current is not None and current.data != item:
            index += 1
            current = current.next
        if current is None:
            return -1
        return index

    def has(self, item):
        if self.index(item) >= 0:
            return True
        return False

    def pop(self, index=None):
        if index is not None and index >= self.size:
            raise IndexError("Out of range.")

        current = self.__head
        previous = None

        if index is None:
            while current.next is not None:
                previous = current
                current = current.next
        else:
            while current.next is not None and index > 0:
                previous = next
                current = current.next
                index -= 1
        self.updatePointers(previous, current)
        self.__size -= 1
        return current.data


class UnorderedList(List):
    def __init__(self, item=None):
        super().__init__()
        self.__tail = None
        if item is not None:
            self.append(item)

    def __str__(self):
        return "Unordered List(" + str(self.size) + "): " + self.__repr__()

    def append(self, item, end="rear"):
        if end not in ["front", "rear"]:
            raise ValueError("\"" + str(end) + "\"",
                             "is not a valid end (front or rear) of the list")

        new = Node(item)
        if end == "front":
            if self.head is None:
                self.__tail = new
            else:
                new.next = self.head
            self.head = new
        else:
            if self.__tail is None:
                self.head = new
            else:
                self.__tail.next = new
            self.__tail = new
        self.size = self.size + 1

    def insert(self, index, item):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Only non-negative integers valid indices")
        if index >= self.__size:
            raise IndexError("Out of range")

        new = Node(item)
        next = self.head
        previous = None

        while next is not None and index > 0:
            previous = next
            next = next.next
            index -= 1

        new.next = next
        if previous is None:
            self.head = new
        else:
            previous.next = new
        if next is None:
            self.__tail = new
        self.size = self.size + 1

    def updatePointers(self, previous, current):
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
            if current.next is None:
                self.__tail = previous

    def remove(self, item):
        if self.isEmpty():
            raise IndexError("List is empty.")

        current = self.head
        previous = None
        while current is not None and current.data != item:
            previous = current
            current = current.next

        if current is None:
            raise ValueError("Item not found.")
        self.updatePointers(previous, current)
        self.size = self.size - 1

    def slice(self, *argv):
        if len(argv) < 1 or len(argv) > 2:
            raise ValueError(
                "Method uses at most a start and and a stop index or, at least, a stop index to perform the slice.")
        if len(argv) == 1:
            if argv[0] > self.size:
                raise IndexError("Stop index greater than list's size.")
        else:
            if argv[1] < argv[0]:
                raise IndexError("Stop index precedes the start index.")
            if not argv[0] < self.size:
                raise IndexError("Start index beyond last index.")
            if argv[1] > self.size:
                raise IndexError("Stop index greater than list's size.")
        for index in argv:
            if index < 0:
                raise IndexError("Negative indexes are not accepted.")

        result = UnorderedList()
        current = self.head
        start = argv[0] if len(argv) == 2 else 0
        stop = argv[0] if len(argv) == 1 else argv[1]
        i = 0

        while i < start:
            current = current.next
            i += 1
        while i < stop:
            result.append(current.data)
            current = current.next
            i += 1
        return result


class OrderedList(List):
    def __init__(self, item=None):
        super().__init__()
        if item is not None:
            self.insert(item)

    def __str__(self):
        return "Ordered List(" + str(self.size) + "): " + self.__repr__()

    def insert(self, item):
        new = Node(item)
        next = self.head
        previous = None

        while next is not None and next.data < item:
            previous = next
            next = next.next

        new.next = next
        if previous is None:
            self.head = new
        else:
            previous.next = new
        self.size = self.size + 1

    def updatePointers(self, previous, current):
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if current is None or current.data != item:
            return False
        self.pdatePointers(previous, current)
        self.size = self.size - 1
        return True

    def slice(self, *argv):
        if len(argv) < 1 or len(argv) > 2:
            raise ValueError(
                "Method uses at most a start and and a stop index or, at least, a stop index to perform the slice.")
        if len(argv) == 1:
            if argv[0] > self.size:
                raise IndexError("Stop index greater than list's size.")
        else:
            if argv[1] < argv[0]:
                raise IndexError("Stop index precedes the start index.")
            if not argv[0] < self.size:
                raise IndexError("Start index beyond last index.")
            if argv[1] > self.size:
                raise IndexError("Stop index greater than list's size.")
        for index in argv:
            if index < 0:
                raise IndexError("Negative indexes are not accepted.")

        result = OrderedList()
        current = self.head
        start = argv[0] if len(argv) == 2 else 0
        stop = argv[0] if len(argv) == 1 else argv[1]
        i = 0

        while i < start:
            current = current.next
            i += 1
        while i < stop:
            result.insert(current.data)
            current = current.next
            i += 1
        return result
