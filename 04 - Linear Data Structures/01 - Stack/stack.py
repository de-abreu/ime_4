class Stack:

    def __init__(self, items=[]):
        self.items = list(items)

    def __str__(self):
        return str(self.peek())

    def __repr__(self):
        return "Stack({}): {}".format(self.size, self.peek())

    def __eq__(self, other):
        return self.size == other.size

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    def push(self, items):
        self.items.append(items)

    def pop(self, index=None):
        if index is None:
            return self.items.pop()
        return self.items.pop(index)

    def peek(self):
        if len(self.items) == 0:
            return []
        return self.items[-1]

    def size(self):
        return len(self.items)


def isBalaced(string):
    s = Stack()

    for c in string:
        if c in "([{":
            s.push(c)
        elif c in ")]}" and (s.size == 0 or not matches(s.pop(), c)):
            return False
    return True


def matches(left, right):
    return "([{".index(left) == ")]}".index(right)
