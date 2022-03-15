class Stack:

    def __init__(self, items=[]):
        self.items = list(items)

    def __str__(self):
        return str(self.peek())

    def __repr__(self):
        return "Stack({}): {}".format(self.size, self.peek())

    def __eq__(self, other):
        return self.items == other.items

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


def parse(str):
    result = []
    word = False

    for c in str:
        if c in " +-*/()":
            word = False
            if c != ' ':
                result.append(c)
        elif not word:
            result.append(c)
            word = True
        else:
            result[-1] += c
    return result


def postfix(expression):

    expression = parse(expression)
    op_stack = Stack()
    op_tokens = {'==': 1, '!=': 1, '<': 1, '>': 1,
                 '<=': 1, '>=': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
    result = []

    for token in expression:
        if token in op_tokens:
            while op_stack.size() > 0 and op_tokens.get(op_stack.peek(), 0) >= op_tokens[token]:
                result.append(op_stack.pop())
            op_stack.push(token)

        elif token == '(':
            op_stack.push(token)

        elif token == ')':
            while(op_stack.peek() != '('):
                result.append(op_stack.pop())
            op_stack.pop()

        else:
            result.append(token)

    while op_stack.size() > 0:
        result.append(op_stack.pop())
    return " ".join(result)


def solve(postfix):
    postfix = postfix.split()
    op_stack = Stack()

    for token in postfix:
        if token in ['+', '-', '*', '/', '^', '==', '!=', '<', '>', '<=', '>=']:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            if token == '^':
                op_stack.push(str(eval(op1 + "**" + op2)))
            else:
                op_stack.push(str(eval(op1 + token + op2)))
        else:
            op_stack.push(token)

    return op_stack.pop()


def main():
    print("This program converts an infix mathematical expression to it postfix form.")

    expression = postfix(input("Type in an expression: "))
    print("Postfix expression: ", expression)
    print("Result form evaluated expression: ", solve(expression))


main()
