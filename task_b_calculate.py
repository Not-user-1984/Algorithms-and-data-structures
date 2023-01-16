import operator

# ID 78867306

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('стек пуст')


def calculate(data, converter=int, stack=None, operations=OPERATORS):
    stack = Stack() if stack is None else stack
    for element in data:
        if element in operations:
            value1, value2 = stack.pop(), stack.pop()
            stack.push(operations[element](value2, value1))
        else:
            try:
                stack.push(converter(element))
            except ValueError:
                raise ValueError(
                    f"Переданное значение - {element} : не может использоваться для вычислений."
                )
    return stack.pop()


if __name__ == '__main__':
    print(calculate(input().split()))
