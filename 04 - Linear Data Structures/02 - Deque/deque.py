from enum import Enum
from enum import auto


class End(Enum):
    front = auto()
    end = auto()


class Deque:

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            items = list(items)
            self.items = items

    def __repr__(self):
        return "Deque({}): front ({}), rear ({})".format(self.size, self.peek(End.front), self.peek(End.rear))

    def __eq__(self, other):
        return self.size == other.size

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    def push(self, item, end=End.rear):
        if end == End.front:
            self.items.insert(0, item)
        else:
            self.items.append(item)

    def pop(self, end=End.rear):
        if self.items == []:
            return []
        if end == End.front:
            return self.items.pop(0)
        return self.items.pop()

    def peek(self, end=End.rear):
        if self.items == []:
            return self.items
        if end == End.front:
            return self.items[0]
        return self.items[-1]

    def size(self):
        return len(self.items)
