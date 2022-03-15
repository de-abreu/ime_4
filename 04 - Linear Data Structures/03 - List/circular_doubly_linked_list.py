class DNode:
    """A doubly-linked node"""

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    data = property(get_data, set_data)

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev = node

    prev = property(get_prev, set_prev)

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    next = property(get_next, set_next)

    def free(self):
        self.next.prev = self.prev
        self.prev.next = self.next

    def __str__(self):
        next = None if self.__next is None else self.__next.data
        prev = None if self.__prev is None else self.__prev.data
        return "{}; previous: {}; next: {};".format(self.__data, next, prev)

    def __repr__(self):
        return str(self.__data)


class CList:
    """A circular, doubly-linked ordered list."""

    def __init__(self, item=None):
        self.__head = DNode(None)
        self.__head.next = self.__head.prev = self.__head
        self.__size = 0

        if item is not None:
            self.insert(item)

    def __len__(self):
        return self.__size

    def __iter__(self):
        current = self.__head.next
        while current is not self.__head:
            yield current.data
            current = current.next

    def __reversed__(self):
        current = self.head.prev
        while current is not self.__head:
            yield current.data
            current = current.prev

    def __repr__(self):
        return str([x for x in self])

    def __str__(self):
        return "Circular List (size {}): {}".format(len(self), self.__repr__())

    def __eq__(self, other):
        return len(self) == len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __add__(self, other):
        result = CList()

        for item in self:
            result.insert(item)
        for item in other:
            result.insert(item)
        return result

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise ValueError("Multiplier is not an integer value.")
        result = CList()

        for item in self:
            for i in range(multiplier):
                result.insert(item)
        return result

    def __find_Node(self, index):
        if index >= len(self) or index < -len(self):
            raise IndexError("Out of range.")
        if index < 0:
            index += len(self)
        if len(self) - index <= index:
            index = len(self) - 1 - index
            current = self.__head.prev
            while index > 0:
                current = current.prev
                index -= 1
        else:
            current = self.__head.next
            while index > 0:
                current = current.next
                index -= 1
        return current

    def __getitem__(self, index=-1):
        if type(index) is int:
            return self.__find_Node(index).data
        elif type(index) is slice:
            result = CList()

            start = 0 if index.start is None else index.start
            if start < 0:
                start += len(self)
            if start >= len(self):
                return result

            stop = len(self) if index.stop is None else index.stop
            if stop < 0:
                stop += len(self)
            if stop <= start:
                return result

            step = 1 if index.step is None else index.step
            if step < 1:
                raise ValueError("Slice step cannot be less than 1.")

            current = self.__head.next
            i = 0
            while i < start:
                current = current.next
                i += 1
            while i < stop:
                result.insert(current.data)
                for j in range(step):
                    current = current.next
                i += step
            return result
        else:
            raise TypeError(
                "Only integers and slices are accepted as indices.")

    def __delitem__(self, index):
        self.__find_Node(index).free()

    def __setitem__(self, index, item):
        current = self.__find_Node(index)
        current.data = self.__head.data = item

        while current.prev.data > current.data:
            prev = current.prev
            prev.next = current.next
            current.prev = prev.prev
            current.next = prev
            prev.prev = current
        while current.next.data < current.data:
            next = current.next
            next.prev = current.prev
            current.next = next.next
            current.prev = next
            next.next = current

    def isEmpty(self):
        return self.__head.next is self.__head

    def index(self, item):
        self.__head.data = item
        current = self.__head.next
        index = 0

        while current.data < item:
            index += 1
            current = current.next
        if current is self.__head or current.data != item:
            return -1
        return index

    def has(self, item):
        if self.index(item) >= 0:
            return True
        return False

    def insert(self, item):
        self.__head.data = item
        new = DNode(item)

        if self.__head.prev.data <= item:
            next = self.__head
        else:
            self.__head.data = item
            next = self.__head.next

            while next.data <= item:
                next = next.next

        new.next = next
        new.prev = next.prev
        new.next.prev = new.prev.next = new
        self.__size += 1

    def pop(self, index=-1):
        current = self.__find_Node(index)

        current.free()
        self.__size -= 1
        return current.data

    def remove(self, item):
        self.__head.data = item
        current = self.__head.next

        while current.data < item:
            current = current.next

        if current is self.__head:
            raise ValueError("Item not found.")

        current.free()
        self.__size -= 1
