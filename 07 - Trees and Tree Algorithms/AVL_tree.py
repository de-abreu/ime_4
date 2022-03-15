class AVLTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __eq__(self, other):
        return len(self) == len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __setitem__(self, key, data):
        if self.__root:
            increment = [0]
            self.__root = self.__root.insert(key, data, increment)
            self.__size += increment[0]
        else:
            self.__root = self.Node(key, data)
            self.__size += 1

    def __getitem__(self, key):
        if not (self.__root and self.__root[key]):
            raise KeyError("Key not found")
        return self.__root[key]

    def __contains__(self, key):
        if not (self.__root and self.__root[key]):
            return False
        return True

    def __delitem__(self, key):
        if not self.__root:
            raise IndexError("Tree is empty")
        self.__root = self.__root.remove(key)
        self.__size -= 1

    def __repr__(self):
        return repr(self.__root)

    def __iter__(self):
        if self.__root:
            yield from self.__root

    def __reversed__(self):
        if self.__root:
            yield from reversed(self.__root)

    def __str__(self):
        return "AVL Tree (size {}): {}".format(len(self), repr(self))

    def get_value(self, k):
        if not isinstance(k, int):
            raise ValueError("Not an integer value")
        if k < 0 or k >= len(self):
            raise IndexError("Index out of range")
        i = [-1]
        return str(self.__root.kthNode(i, k))

    def pre_order(self):
        if self.__root:
            return self.__root.pre_order()
        return ''

    class Node:
        def __init__(self, key, data):
            self.key = int(key)
            self.data = data
            self.height = 0
            self.lt = None
            self.gt = None

        # Information display methods

        def __str__(self):
            return str((self.key, self.data))

        def __repr__(self):
            string = ""
            if self.lt:
                string += repr(self.lt)
            string += str(self) + " "
            if self.gt:
                string += repr(self.gt)
            return string

        def pre_order(self):
            string = str((self.key, self.data)) + " "
            if self.lt:
                string += self.lt.pre_order()
            if self.gt:
                string += self.gt.pre_order()
            return string

        def kthNode(self, index, k):
            lt = None
            if self.lt:
                lt = self.lt.kthNode(index, k)
            if lt:
                return lt
            index[0] += 1
            if index[0] == k:
                return self
            if self.gt:
                return self.gt.kthNode(index, k)
            return None

        # Node insertion method

        def insert(self, key, data, increment):
            if key == self.key:
                self.data = data
                return self
            if key < self.key:
                if self.lt:
                    self.lt = self.lt.insert(key, data, increment)
                else:
                    self.lt = AVLTree.Node(key, data)
                    increment[0] += 1
            else:
                if self.gt:
                    self.gt = self.gt.insert(key, data, increment)
                else:
                    self.gt = AVLTree.Node(key, data)
                    increment[0] += 1
            return self.balance_tree()

        # Node data retrieval methods

        def __getitem__(self, key):
            if key == self.key:
                return self.data
            if key < self.key:
                if not self.lt:
                    return None
                return self.lt[key]
            if not self.gt:
                return None
            return self.gt[key]

        def __iter__(self):
            if self.lt:
                yield from self.lt
            yield self.data
            if self.gt:
                yield from self.gt

        def __reversed__(self):
            if self.gt:
                yield from reversed(self.gt)
            yield self.data
            if self.lt:
                yield from reversed(self.lt)

        # Node removal methods

        def remove(self, key):
            if key == self.key:
                self = self.child
                if self:
                    return self.balance_tree()
            else:
                self = self.remove_child(key)
            return self

        def remove_child(self, key):
            if key < self.key:
                if not self.lt:
                    raise KeyError("Key not found")
                if self.lt.key == key:
                    self.lt = self.lt.child
                else:
                    self.lt = self.lt.remove_child(key)
            else:
                if not self.gt:
                    raise KeyError("Key not found")
                if self.gt.key == key:
                    self.gt = self.gt.child
                else:
                    self.gt = self.gt.remove_child(key)
            return self.balance_tree()

        def __get_child(self):
            if self.lt:
                if not self.gt:
                    return self.lt
                return self.__select_by_key()
            return self.gt

        child = property(__get_child)

        def __select_by_key(self):
            parent, child = self.max_key(self.lt)

            self.__rearrage_nodes(parent, child)
            return child

        def max_key(self, child):
            if not child.gt:
                return (self, child)
            child.max_key(child.gt)

        def __rearrage_nodes(self, parent, child):
            child.gt = self.gt
            if self is parent:
                return
            parent.gt = child.lt
            child.lt = self.lt

        # Tree balancement methods

        def balance_tree(self):
            balance = self.balance

            # Left heavy
            if balance > 1:
                if self.lt.balance < 0:
                    self.lt = self.lt.rotate_left()
                return self.rotate_right()

            # Right heavy
            if balance < -1:
                if self.gt.balance > 0:
                    self.gt = self.gt.rotate_right()
                return self.rotate_left()

            self.update_height()
            return self

        def __get_height(self, root):
            return root.height if root else -1

        def __get_balance(self):
            return self.__get_height(self.lt) - self.__get_height(self.gt)

        balance = property(__get_balance)

        def update_height(self):
            self.height = max(self.__get_height(self.lt),
                              self.__get_height(self.gt)) + 1

        def rotate_left(self):
            substitute = self.gt
            child = substitute.lt

            substitute.lt = self
            self.gt = child

            self.update_height()
            substitute.update_height()
            return substitute

        def rotate_right(self):
            substitute = self.lt
            child = substitute.gt

            substitute.gt = self
            self.lt = child

            self.update_height()
            substitute.update_height()
            return substitute
