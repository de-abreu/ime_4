class BinaryHeap:
    def __init__(self, item=None):
        if item is None:
            self.__heap = []
        elif isinstance(item, list):
            self.__heap = item[:]
            for i in range((len(item) - 1) // 2, -1, -1):
                self.__perc_down(i)
        else:
            self.__heap = [item]

    def __len__(self):
        return len(self.__heap)

    def __eq__(self, other):
        return len(self) == len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __iter__(self):
        return self.__heap.__iter__()

    def __repr__(self):
        return str(list(self))

    def __str__(self):
        return "Heap (size {}): {}".format(len(self), self.__repr())

    def __getitem__(self, index):
        return self.__heap[index]

    def __perc_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self[parent] < self[index]:
            return
        self.__heap[parent], self.__heap[index] = self[index], self[parent]
        self.__perc_up(parent)

    def insert(self, item):
        self.__heap.append(item)
        self.__perc_up(len(self) - 1)

    def __perc_down(self, index):
        minimal = index
        left = 2 * minimal + 1
        right = left + 1

        if left >= len(self):
            return
        if self[left] < self[minimal]:
            minimal = left
        if right < len(self) and self[right] < self[minimal]:
            minimal = right
        elif minimal == index:
            return

        self.__heap[index], self.__heap[minimal] = self[minimal], self[index]
        self.__perc_down(minimal)

    def pop(self):
        if len(self) == 0:
            raise IndexError("heap is empty")
        self.__heap[0], self.__heap[-1] = self[-1], self[0]
        item = self.__heap.pop()
        self.__perc_down(0)
        return item
