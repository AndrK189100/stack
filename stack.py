
class Stack:

    def __init__(self):
        self._stack = list()

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        try:
            self._stack.pop()
        except IndexError:
            return 'stack is empty'

    def peek(self):
        try:
            return self._stack[len(self._stack) - 1]
        except IndexError:
            return 'stack is empty'

    def size(self):
        if self._stack:
            return len(self._stack)
        else:
            return 0

    def isEmpty(self):
        return True if not self._stack else False




