from stack import Stack

fixture = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


def is_balanced_brackets(brackets: str) -> str:

    if len(brackets) % 2 != 0 or len(brackets) < 2 or brackets[0] not in ('(', '{', '['):
        return 'Несбалансированно'

    stack = Stack()
    stack.push(brackets[0])

    i = 1

    while i < len(brackets):

        if ord(stack.peek()) == ord(brackets[i]) - 1 or ord(stack.peek()) == ord(brackets[i]) - 2:
            stack.pop()
            if stack.isEmpty():
                i += 1
                if i == len(brackets):
                    break
                stack.push(brackets[i])
                i += 1
            else:
                i += 1
        else:
            stack.push(brackets[i])
            i += 1

    return 'Сбалансированно' if stack.isEmpty() else 'Несбалансированно'


if __name__ == '__main__':

    for item in fixture:
        print(is_balanced_brackets(item))
