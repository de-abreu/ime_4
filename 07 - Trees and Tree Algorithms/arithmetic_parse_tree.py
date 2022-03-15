class BinaryTree:
    def __init__(self, item=None):
        if item:
            self.__root = self.Node(item)
            self.__size = 1
        else:
            self.__root = None
            self.__size = 0

    def __len__(self):
        return self.__size

    def __str__(self):
        return "Binary Tree (size {}): {}".format(len(self), str(self.__root))

    def __repr__(self):
        return repr(self.__root)

    def __get__(self):
        return self.__root

    def __set__(self, item):
        self.__root = item

    def __get_left(self):
        return self.__root.left

    def __set_left(self, item):
        self.__root.left = item

    def __del_left(self):
        del self.__root.left

    left = property(__get_left, __set_left, __del_left, "Left node")

    def __get_right(self):
        return self.__root.right

    def __set_right(self, item):
        self.__root.right = item

    def __del_right(self):
        del self.__root.right

    right = property(__get_right, __set_right, __del_right, "Right node")

    def insert(self, item, side="left"):
        if side not in ("left", "right"):
            raise ValueError("side is neighter left nor right")
        if not self.__root:
            self.__root = self.Node(item)
        elif side == "left":
            self.__root.insert_left(item)
        else:
            self.__root.insert_right(item)
        self.__size += 1

    class Node:
        def __init__(self, item):
            self.__item = item
            self.__left = None
            self.__right = None

        def __get__(self):
            return self.__item

        def __set__(self, item):
            self.__item = item

        def __get_left(self):
            return self.__left

        def __set_left(self, item):
            if self.__left:
                self.__left.__set__(item)
            else:
                self.__left = BinaryTree.Node(item)

        def __del_left(self):
            self.__left = None

        left = property(__get_left, __set_left, __del_left, "Left node")

        def __get_right(self):
            return self.__right

        def __set_right(self, item):
            if self.__right:
                self.__right.__set__(item)
            else:
                self.__right = BinaryTree.Node(item)

        def __del_right(self):
            self.__right = None

        right = property(__get_right, __set_right, __del_right, "Right node")

        def __str__(self):
            return "Node({}): left({}), right({})".format(self.__item,
                                                          self.__left,
                                                          self.__right)

        def __repr__(self):
            string = str(self.__item)
            if self.__left or self.__right:
                string += " : ({}), ({})".format(repr(self.__left),
                                                 repr(self.__right))
            return string

        def insert_left(self, item):
            if self.__left:
                new_child = BinaryTree.Node(item)
                new_child.left, self.left = self.left, new_child
            else:
                self.__left = BinaryTree.Node(item)

        def insert_right(self, item):
            if self.__right:
                new_child = BinaryTree.Node(item)
                new_child.right, self.right = self.right, new_child
            else:
                self.__right = BinaryTree.Node(item)
